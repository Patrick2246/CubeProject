#import libraries
import pygame, sys, time, random
pygame.init()
#setup screen size for game
window=pygame.display.set_mode((500,500))
pygame.display.set_caption("Cube.io Game")
cubeSize=10
#RGB colors
yellow=(255,255,0)
myColor=(255,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(45,252,222)
bigColor=(0,0,0)
food=[random.randrange(1,500), random.randrange(1,500),10,10]
bfood=[random.randrange(1,500),random.randrange(1,500),10,10]
#X and Y position of the red cube
speed=5
cubeX=250
cubeY=250
#variable to control the game
run=True
cube=pygame.Rect(cubeX,cubeY,cubeSize,cubeSize)
food_status=True
bfood_status=True
while run:
  pygame.time.delay(10)
  window.fill(white)
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      run=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
      if cubeX>=480:
        cubeX=480
      else:
        cubeX+=speed
    if keys[pygame.K_LEFT]:
      if cubeX<=0:
        cubeX=0
      else:
        cubeX-=speed
    if keys[pygame.K_DOWN]:
      if cubeY>=480:
        cubeY=480
      else:
        cubeY-=speed
    if keys[pygame.K_UP]:
      if cubeY<=0:
        cubeY=0
      else:
        cubeY+=speed 
  cube=pygame.Rect(cubeX,cubeY,cubeSize,cubeSize)
  #draw the cube
  if cubeSize<=100:
    pygame.draw.rect(window,myColor,cube)
  else:
    pygame.draw.rect(window,bigColor,cube)
  #checking collision with good food
  if cube.colliderect(food):
    cubeSize+=10
    food_status=False
  #checking collision with bad food
  if cube.colliderect(bfood):
    cubeSize-=10
    bfood_status=False
  #spawn good food
  if food_status==False:
    food=[random.randrange(1,500),random.randrange(1,500),10,10]
    food_status=True
  #spawn bad food
  if bfood_status==False:
    bfood=[random.randrange(1,500),random.randrange(1,500),10,10]
    bfood_status=True
  pygame.draw.rect(window,green,pygame.Rect(food))
  pygame.draw.rect(window,yellow,pygame.Rect(bfood))
  pygame.display.update()
pygame.quit()