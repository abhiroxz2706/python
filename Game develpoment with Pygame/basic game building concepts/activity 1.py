import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,225), pygame.Rect(70,150,180,60),5)

    pygame.display.flip()