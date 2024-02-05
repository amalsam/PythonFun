import pygame,random,sys

pygame.init()
WIDTH = 800
HEIGHT =500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

all_lifes = pygame.sprite.Group()

class Life(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5,5])
        self.image.fill("black")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alive = False
        self.neighbour = 0

    def update(self):
        if self.alive:
            self.image.fill("white")
        else :
            self.image.fill("black")
        self.neighbour = 0
        self.is_neighbour_alive(-1,-1)
        self.is_neighbour_alive(0,-1)
        self.is_neighbour_alive(1,-1)
        self.is_neighbour_alive(-1,0)
        self.is_neighbour_alive(1,0)
        self.is_neighbour_alive(-1,1)
        self.is_neighbour_alive(0,1)
        self.is_neighbour_alive(1,1)

    def update_state(self):
        if self.neighbour>= 4 or self.neighbour<=1:
            self.alive = False
        if self.neighbour == 3:
            self.alive = True

        
        

        

    def is_neighbour_alive(self,x,y):
        try:
            if life[self.rect.x//5 + x][self.rect.y//5 + y].alive:
                self.neighbour += 1
        except:
            None


life = []

for i,x in enumerate(range(0,WIDTH,5)):
    a = []
    for j,y in enumerate(range(0,HEIGHT,5)):
        a.append(Life(x,y))
        all_lifes.add(a[j])

    life.append(a)


def game_loop():
    pause =True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                life[mouse_x//5][mouse_y//5].alive = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pause = False
                elif event.key == pygame.K_SPACE:
                    pause = True

        all_lifes.update()
        if not pause:
            pygame.display.set_caption("PRESS SPACE TO PAUSE")
            for x in range(0,WIDTH//5):
                for y in range(0,HEIGHT//5):
                    life[x][y].update_state()
        if pause:
            pygame.display.set_caption("PAUSED >>>>>> PRESS ENTER TO START")
        
              
        screen.fill("blue")
        all_lifes.draw(screen)
        clock.tick(5)
        
        pygame.display.update()

game_loop()

