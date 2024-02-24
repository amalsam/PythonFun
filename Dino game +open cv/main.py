import pygame

import sys

import math
import random
from pygame.locals import *
import mediapipe as mp
import cv2



pygame.init()
clock = pygame.time.Clock()


#Getting mediapipe: Hands ready
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#Capture webcam
cam = cv2.VideoCapture(0)

# Options
WINDOW_SIZE = (800,800) # (Width, Height)
DRAW_LINES = False # (Draw lines between the dinosaur and cactus to see what the AI sees)

screen = pygame.display.set_mode(WINDOW_SIZE)


GROUND_LEVEL = WINDOW_SIZE[1]/2 + 75
ground_rect = pygame.Rect(0, GROUND_LEVEL, WINDOW_SIZE[0], WINDOW_SIZE[1])

dinosaur_img = pygame.image.load('data/dino1.png').convert_alpha()
cactus_img = pygame.image.load('data/cactus.png').convert_alpha()
font = pygame.font.Font('data/roboto.ttf', 25)

generation = 0

class Dinosaur():
    def __init__(self, x, y, width, height, img): #img must be a pygame surface object
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.transform.scale(img, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.vertical_momentum = 0
        self.onGround = False
        self.last_closest_pipe = cacti[0] # Setting the closest cactus to the leftmost cactus by default

    def update(self):
        self.x, self.y = self.rect.x, self.rect.y # Updating position atributes
        self.movement()

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def jump(self):
        if self.onGround:
            self.vertical_momentum = -12

    def movement(self):
        self.rect.y += self.vertical_momentum

        if self.rect.colliderect(ground_rect):
            self.onGround = True
        else:
            self.onGround = False

        if self.onGround:
            self.rect.bottom = ground_rect.top + 1 # Adding 1 so that the dinosaur continues to collide with the rect, instead of shaking up and down
            # Prevent from falling through the ground
            self.vertical_momentum = 0
        else:
            # Add gravity
            self.vertical_momentum += 0.5

        # Cap gravity
        if self.vertical_momentum >= 40:
            self.vertical_momentum = 40

class Cactus():
    def __init__(self, x, y, width, height, img, scroll_speed = 7):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scroll_speed = scroll_speed
        self.img = pygame.transform.scale(img, (width, height))
        self.rect = pygame.Rect(x, y, width, height)

    def update(self):
        self.x -= self.scroll_speed # Moves cactus to the left
        self.rect.x, self.rect.y = self.x, self.y # Update position atributes

    def draw(self):
        screen.blit(self.img, (self.x, self.y))




    
    
    

def thumbs_up_detected(x, y):
    # Assuming thumb landmark is at index 4 and index finger landmark is at index 8
    thumb_tip_x = x[4]
    thumb_tip_y = y[4]
    index_finger_tip_x = x[8]
    index_finger_tip_y = y[8]
    
    # Check if thumb is above index finger tip
    if thumb_tip_y < index_finger_tip_y:
        # Check if thumb is to the right of index finger tip
        if thumb_tip_x > index_finger_tip_x:
            return True
    
    return False

    

def main():
    global cacti, dinosaur
    cacti = [Cactus(WINDOW_SIZE[0] + 100, GROUND_LEVEL - 86, 50, 86, cactus_img)]
    

    scroll_speed = 5
    dinosaur=Dinosaur(100, GROUND_LEVEL-90, 50, 50, dinosaur_img)
    run = True

    while run:
        screen.fill('white')
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dinosaur.jump()


        #Set up the hand tracker
        success, img = cam.read()
        imgg = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(imgg, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = imgg.shape
                    if id == 0:
                        x = []
                        y = []
                    x.append(int((lm.x) * w))
                    y.append(int((1 - lm.y) * h))

                    #This will track the hand gestures
                    
                # if thumbs_up_detected(x, y):
                #     dinosaur.jump()
                if ((y[8] > y[7])):
                    dinosaur.jump()
                           
                        # if not(x[0] > x[3] > x[4]) and (y[20] > y[17]):
                        #     dinosaur.jump()
                        # if (x[0] > x[3] > x[4]) and (y[20] > y[17]):
                        #     dinosaur.jump()

                mpDraw.draw_landmarks(imgg, handLms, mpHands.HAND_CONNECTIONS)


        cv2.namedWindow("WebCam")
        cv2.moveWindow("WebCam", 20, 121)
        cv2.imshow("WebCam", imgg)
        cv2.waitKey(1)

        
        

        # Adding new cactus
        if len(cacti) <= 1:
            if cacti[0].x < random.randint(100, WINDOW_SIZE[0] - 300) + scroll_speed:
                cacti.append(Cactus(WINDOW_SIZE[0] + 100, GROUND_LEVEL - 86, 50, 86, cactus_img, scroll_speed))

        for cactus in cacti:
            cactus.draw()
            cactus.update()
            if cactus.x < -100:
                cacti.remove(cactus)
            if dinosaur.rect.colliderect(cactus.rect):
                main()
            
        
        dinosaur.update()
        
           
        # for cactus in cacti:
        #     cactus.scroll_speed += 0.05
        #     scroll_speed += 0.05 

        pygame.draw.line(screen, (75, 75, 75), (0, GROUND_LEVEL), (WINDOW_SIZE[0], GROUND_LEVEL), 3)
        dinosaur.draw()
        
        pygame.display.update()
        pygame.display.set_caption(str(clock.get_fps()))
        clock.tick(24)


main()


