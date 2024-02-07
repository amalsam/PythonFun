import pygame
import sys,random

#initialize pygame
pygame.init()

#constents
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
SQUARE_SIZE = WIDTH // GRID_SIZE

#initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#initialize clock,this clock is used to controll fps
clock = pygame.time.Clock()


def draw_board(queens):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if (row + col) % 2 == 0:
                color = "white"
            else:
                color = "black"
            pygame.draw.rect(screen, color, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            #if (row,col) not in safe_board(queens):
            #pygame.draw.rect(screen, (0,0,200,0.9), (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            


#display all queens inside list
def draw_queens(queens):
    for i in queens:
        row = i[0] 
        col = i[1]
        pygame.draw.circle(screen, "red", ((row * SQUARE_SIZE) + SQUARE_SIZE // 2, (col * SQUARE_SIZE) + SQUARE_SIZE // 2), SQUARE_SIZE // 3)


#this function returns a list that consist of all safe boxes
def safe_board(queens):
    global deleted_queen
    safe = []
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if is_safe(x,y,queens) and (x,y) != deleted_queen:
                safe.append((x,y))
    return safe


#add a random safe co-ordinate to queens list
def add_queen(queens,safe):
    if len(safe) == 0 and len(queens)<GRID_SIZE:
        
        backtrack(queens)
    if len(safe) > 0:
        queens.append(random.choice(safe))
    

    
deleted_queen = None
backtrackno = 1
pop_count =1

#function for backtrack
def backtrack(queens):
    global deleted_queen,backtrackno,pop_count
    backtrackno+=1

    if backtrackno > pop_count*GRID_SIZE:
        backtrackno =1
        pop_count+=1
    for i in range(pop_count):
        deleted_queen = (queens[-1])
        queens.pop()
    safe = safe_board(queens)
    add_queen(queens,safe)
    
               
#checking a box safe or not
def is_safe(x,y,queens):
    for i in queens:
        row = i[0]
        col = i[1]

        if x == row: 
            return False
        
        if y == col:  
            return False

        if row-col == x- y:
            return False
        
        if GRID_SIZE-row-col == GRID_SIZE-x-y:
            return False
    return True

# Main function
def main():
    first_click = True
    queens = []
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and first_click:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                queens.append((mouse_x//SQUARE_SIZE,mouse_y//SQUARE_SIZE))
                first_click = False
                
        safe = safe_board(queens)
        screen.fill("white")
        draw_board(queens)
        draw_queens(queens)
        if not first_click:
            add_queen(queens,safe)
        pygame.display.update()
        clock.tick(60)

main()

    