import pygame
pygame.init()

Black=(0,0,0)
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Pygame activity")
background=pygame.image.load("lbg.jpg")
background=pygame.transform.scale(background, (500,500))
character=pygame.image.load("im.jpg")
character=pygame.transform.scale(character, (100,150))
font=pygame.font.Font(None,50)
text=font.render("Hello",True,Black)
character_x=0
character_y=0
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            running=False
    screen.blit(background,(0,0))
    screen.blit(character,(character_x,character_y))
    screen.blit(text,(200,100))
    pygame.display.flip()