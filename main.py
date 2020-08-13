import pygame
import time
import random

pygame.init()

white = (0, 0, 0)
black = (0, 0, 0)
red = (213, 50, 800)
yellow = (255, 255, 130)
green = (0, 255, 0)
blue = (50,153,213)

diswidth = 600
disheight = 400

dis = pygame.display.set_mode(( diswidth, disheight))
pygame.display.set_caption("SnAk GaM")

clock = pygame.time.Clock()

snakeblock = 10
snakespeed = 15

fontstyle = pygame.font.SysFont('bahnschrift', 25)
scorefont = pygame.font.SysFont("comicsan", 35)

def yourscore(score):
  value = scorefont.render("your score: " + str(score),True,yellow)
  dis.blit(value, [0,0])

def oursnake(snakeblock, snakelist):
  for x in snakelist: 
   pygame.draw.rect(dis,black,[x[0],x[1],snakeblock,snakeblock])

def message(msg,color):
  mesg = fontstyle.render(msg, True, color)
  dis.blit(mesg,[diswidth/6,disheight/3])

def gameloop():
  gameover = False
  gameclose = False
  x1 = diswidth/2
  y1 = disheight/2
  x1change = 0
  y1change = 0
  snakelist = []
  lengthofsnake = 1
  foodx = round(random.randrange(0,diswidth-snakeblock)/10)*10
  foody = round(random.randrange(0,disheight-snakeblock)/10)*10

  while not gameover:
    while gameclose:
      dis.fill(blue)
      message("you lost press C to play again Q to quit", red)
      yourscore(lengthofsnake-1)
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            gameover = True
            gameclose = False
          if event.key == pygame.K_c:
              gameloop()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        gameover = True
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          x1change = -snakeblock
          y1change = 0
        elif event.key == pygame.K_RIGHT:#right movement
          x1change = snakeblock
          y1change = 0
        elif event.key == pygame.K_UP:#up movement
          x1change = 0
          y1change = -snakeblock
        elif event.key == pygame.K_DOWN:#down movement
          x1change = 0
          y1change = snakeblock 
    if x1 >= diswidth or 0 > x1 or y1 >= disheight or 0 > y1:#if collide wih the wall and lose
      gameclose = True
    x1 += x1change#applying movement
    y1 += y1change#applying movement
    dis.fill(blue)
    pygame.draw.rect(dis, green, [foodx,foody,snakeblock,snakeblock])
    snakehead = []
    snakehead.append(x1)
    snakehead.append(y1)
    snakelist.append(snakehead)

    if len(snakelist) > lengthofsnake:
      del snakelist[0]
    for x in snakelist[:-1]:
      if x == snakehead:
        gameclose = True
    oursnake(snakeblock,snakelist)
    yourscore(lengthofsnake-1)

    pygame.display.update()
  
    if x1 == foodx and y1 == foody:
      foodx = round(random.randrange(0,diswidth-snakeblock)/10)*10
      foody = round(random.randrange(0,disheight-snakeblock)/10)*10
      lengthofsnake += 1
    clock.tick(snakespeed)
  pygame.quit()
  quit()

gameloop()
