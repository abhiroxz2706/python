import pygame
import random
pygame.init()

screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("Colour changing sprite")

sprite_color= pygame.Color("white")
x=random.randint(1,700)
y=random.randint(1,700)
width=12
height=7

colours=["red","blue","yellow","orange","black","pink","grey"]

Color_Change=pygame.USEREVENT + 1

running=True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == Color_Change:
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               sprite_color=pygame.Color(random.choice(colours))
            if event.key == pygame.K_UP:
               y -= 5
            if event.key == pygame.K_RIGHT:
               y += 5
            if event.key == pygame.K_LEFT:
               x -= 5
            if event.key == pygame.K_DOWN:
               y += 5

    pygame.draw.rect(screen,sprite_color(x,y,width,height))
    pygame.draw.rect(screen,sprite_color(x,y,width,height))

    pygame.display.update()

pygame.quit()