import pygame,random,sys

#initialize pygame
pygame.init()

#creating constants
WIDTH,HEIGHT = 600,600
GRID_SIZE = 8 #size of N
SQUARE_SIZE = WIDTH // GRID_SIZE

# global variable
deleted_queen = None
backtrack_count = 1
pop_count = 1

#initialize the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#initialize clock ,this clock is used to controll fps
clock = pygame.time.Clock()


#function to draw board
def draw_board():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if(row + col) % 2 == 0:
                color ="white"
            else:
                color ="black"
            pygame.draw.rect( screen,color,(row * SQUARE_SIZE, col * SQUARE_SIZE , SQUARE_SIZE, SQUARE_SIZE))


#function to draw queens on screen
def draw_queens(queens):
    for i in queens:
        row = i[0]
        col = i[1]
        pygame.draw.circle(screen,
                           "gold",
                           ((row * SQUARE_SIZE)+ SQUARE_SIZE // 2, (col * SQUARE_SIZE) + SQUARE_SIZE //2),
                           SQUARE_SIZE //3)
        

#this function returns all safe boxes inside the board as list
def safe_board(queens):
    global deleted_queen
    safe = []
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if is_safe(x,y,queens) and (x,y) != deleted_queen:
                safe.append((x,y))

    return safe
    

#this function takes coordinate of a square as input and check it is safe or not
def is_safe(x,y,queens):
    for i in queens:
        row = i[0]
        col = i[1]

        if x==row:
            return False
        if y == col :
            return False
        if row - col == x - y:
            return False
        if GRID_SIZE - row - col == GRID_SIZE - x - y:
            return False
    return True          # if safe return True


#this function adds a random safe coordinate to queens list
def add_queen(queens,safe):
    if len(safe) > 0:
        queens.append(random.choice(safe))
    if len(safe) == 0 and len(queens) < GRID_SIZE:
        backtrack(queens)
    


def backtrack(queens):
    global backtrack_count,pop_count,deleted_queen

    backtrack_count += 1
    if backtrack_count > pop_count * GRID_SIZE:
        backtrack_count = 1
        pop_count += 1
    for i in range(pop_count):
        deleted_queen = queens[-1]
        queens.pop()
    safe = safe_board(queens)
    add_queen(queens,safe)
    


def game_loop():
    queens = []
    first_click = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and first_click:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                queens.append((mouse_x//SQUARE_SIZE,mouse_y//SQUARE_SIZE))
                first_click = False

        safe = safe_board(queens)
        screen.fill("white")
        if not first_click:
            add_queen(queens,safe)
        draw_board()
        draw_queens(queens)
        clock.tick(100)
        
        pygame.display.update()


game_loop()
