import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.circle(screen,(200,150,225), (50,50),45)
    pygame.draw.circle(screen,(200,150,225), (350,50),45,7)

    pygame.display.flip()