import psycopg2
import pygame
import time
import random
flag=True
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
a=False
conn=psycopg2.connect(
    host="localhost",
    database="snakescore",
    user="postgres",
    password="29032003"
)
name=input("Enter your name \n")
print(name)
sql=f'select * from SNAKESCORE1 where username = \'{name}\''
cursor = conn.cursor()
cursor.execute(sql)
res=cursor.fetchall()
if not res:
    print("OK")
    b=10
    cursor.execute("INSERT INTO SNAKESCORE1(username,score) VALUES (%s,%s)", (name,b))
    conn.commit()
else:
    if res[0][0]==name:
        a=True
        b=res[0][1]


width = 600
height = 400

dis = pygame.display.set_mode((width,height))

 
clock = pygame.time.Clock()
 
snake_size = 10
if a==True:
    snake_speed=b
else:
    snake_speed=10
font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 35)
velocity_font= pygame.font.SysFont(None, 35)
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, red)
    dis.blit(value, [0, 0])
def Yourspeed(velocity):
    value=velocity_font.render("Velocity: "+str(velocity),True,red)
    dis.blit(value,[200,0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width / 6, height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = width / 2
    y1 = height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
    snake_speed= b
 
    foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
   
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost!", red)
            Yourspeed(snake_speed)
            pygame.display.update()
 
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0
 
        if x1 >=width or x1 < 0 or y1 >=height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx, foody, snake_size, snake_size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_size, snake_List)
        Your_score(Length_of_snake - 1)
    
 
        pygame.display.update()
        Yourspeed(snake_speed)
        pygame.display.update()
 
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed += 1
            
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()