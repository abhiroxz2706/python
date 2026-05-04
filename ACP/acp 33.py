import pygame

pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game screen")

character=pygame.image.load("ir.jpg")
character=pygame.transform.scale(character, (300,300))
character_x=250
character_y=250

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            running=False
    
    screen.fill((58,58,58))
    screen.blit(character,(character_x,character_y))

pygame.quit()