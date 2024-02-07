import pygame
import random
import sys



pygame.init()
HEIGHT = 800;WIDTH=1200

cell_size=10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_life = pygame.sprite.Group()

counter = 50                                     #update-time speed ,in milli sec
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event,counter)


class Life(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([cell_size,cell_size])
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alive = False #random.choices( [True,False], weights=[0.1,0.99] )[0]
        self.neighbor = 0

        
    def update(self):
        if self.alive == False:
            self.image.fill("black")
        else:
            self.image.fill("white")        
        self.neighbor = 0
        self.check_neighbor(-1,-1)
        self.check_neighbor(0,-1)
        self.check_neighbor(1,-1)
        self.check_neighbor(-1,0)
        self.check_neighbor(1,0)
        self.check_neighbor(-1,1)
        self.check_neighbor(0,1)
        self.check_neighbor(1,1)
        


    def check_neighbor(self,x,y):
        try:
            if life[self.rect.x//cell_size + x][ self.rect.y//cell_size + y].alive:
                self.neighbor+=1
        except:
            None

    def update_state(self):
        if self.neighbor>=4 or self.neighbor<=1:
            self.alive = False
        if self.neighbor == 3 and self.alive==False:
            self.alive = True



life =[]
for i,x in enumerate(range(0,WIDTH,cell_size)):
    a = []
    for j,y in enumerate(range(0,HEIGHT,cell_size)):    
        a.append(Life(x,y))
        all_life.add(a[j])
    life.append(a)




def draw_text(surf, text, size, x, y):
    ## selecting a cross platform font to display the score
    font = pygame.font.Font(pygame.font.match_font('arial'), size)
    text_surface = font.render(text, True, "green")       
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



def create_alive_group(x,y):
    life[x][y-1].alive = True
    life[x+1][y].alive = True
    life[x-1][y+1].alive = True
    life[x][y+1].alive = True
    life[x+1][y+1].alive = True

def create_alive_group2(x,y):
    life[x][y+1].alive = True
    life[x-1][y].alive = True
    life[x+1][y-1].alive = True
    life[x][y-1].alive = True
    life[x-1][y-1].alive = True
   

def create_three(x,y):
    life[x+1][y-1].alive = True
    life[x-1][y].alive = True
    life[x][y+1].alive = True
 
def make_alive(x,y,i,j):
    life[x+i][y+j].alive = True
    

def create_shape(x,y):
    make_alive(x,y,0,3)
    make_alive(x,y,0,4)
    make_alive(x,y,1,3)
    make_alive(x,y,1,4)
    make_alive(x,y,10,3)
    make_alive(x,y,10,4)
    make_alive(x,y,10,5)
    make_alive(x,y,11,2)
    make_alive(x,y,11,6)
    make_alive(x,y,12,1)
    make_alive(x,y,12,7)
    make_alive(x,y,13,1)
    make_alive(x,y,13,7)
    make_alive(x,y,14,4)
    make_alive(x,y,15,2)
    make_alive(x,y,15,6)
    make_alive(x,y,16,3)
    make_alive(x,y,16,4)
    make_alive(x,y,16,5)
    make_alive(x,y,17,4)
    make_alive(x,y,20,1)
    make_alive(x,y,20,2)
    make_alive(x,y,20,3)
    make_alive(x,y,21,1)
    make_alive(x,y,21,2)
    make_alive(x,y,21,3)
    make_alive(x,y,22,0)
    make_alive(x,y,22,4)
    make_alive(x,y,24,-1)
    make_alive(x,y,24,0)
    make_alive(x,y,24,4)
    make_alive(x,y,24,5)
    make_alive(x,y,34,1)
    make_alive(x,y,34,2)
    make_alive(x,y,35,1)
    make_alive(x,y,35,2)

def create_shape_negetive(x,y):
    make_alive(x,y,0,-3)
    make_alive(x,y,0,-4)
    make_alive(x,y,-1,-3)
    make_alive(x,y,-1,-4)
    make_alive(x,y,-10,-3)
    make_alive(x,y,-10,-4)
    make_alive(x,y,-10,-5)
    make_alive(x,y,-11,-2)
    make_alive(x,y,-11,-6)
    make_alive(x,y,-12,-1)
    make_alive(x,y,-12,-7)
    make_alive(x,y,-13,-1)
    make_alive(x,y,-13,-7)
    make_alive(x,y,-14,-4)
    make_alive(x,y,-15,-2)
    make_alive(x,y,-15,-6)
    make_alive(x,y,-16,-3)
    make_alive(x,y,-16,-4)
    make_alive(x,y,-16,-5)
    make_alive(x,y,-17,-4)
    make_alive(x,y,-20,-1)
    make_alive(x,y,-20,-2)
    make_alive(x,y,-20,-3)
    make_alive(x,y,-21,-1)
    make_alive(x,y,-21,-2)
    make_alive(x,y,-21,-3)
    make_alive(x,y,-22,0)
    make_alive(x,y,-22,-4)
    make_alive(x,y,-24,1)
    make_alive(x,y,-24,0)
    make_alive(x,y,-24,-4)
    make_alive(x,y,-24,-5)
    make_alive(x,y,-34,-1)
    make_alive(x,y,-34,-2)
    make_alive(x,y,-35,-1)
    make_alive(x,y,-35,-2)






def spawn_big_square(x,y):
     for i in range(0,20):
         for j in range(0,20):
             if i ==j:
                 continue
             life[x + i][y + j].alive =True


def game_loop():
    pause = True
    while True:
        screen.fill("black")  
        all_life.draw(screen)
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pause = False
                if event.key == pygame.K_ESCAPE:
                    pause = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                point = pygame.mouse.get_pos()
                life[point[0]//cell_size][point[1]//cell_size].alive =True

            elif event.type == timer_event:
                all_life.update()

                if (not pause):
                    pygame.display.set_caption("Esc to pause     fps:"+str(int(clock.get_fps())) )
                    for x in range(0,WIDTH//cell_size):
                        for y in range(0,HEIGHT//cell_size):    
                            life[x][y].update_state()


            if pause:    
                pygame.display.set_caption("Paused   use mouse to create cell      enter tor start    fps:"+str(int(clock.get_fps())) )

        pygame.display.update()


if __name__ ==  "__main__":
    
    create_shape(10,10)
    create_shape_negetive(80,50)

    spawn_big_square(80,0)
    #spawn_big_square(10,40)

    	  
    game_loop()


    






    