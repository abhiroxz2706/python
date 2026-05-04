import pygame

pygame.init()
screen_width,screen_height=640,800
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Moving rectangular sprite")


sprite_col=pygame.Color("lightblue")
x,y=320,400
sprite_width,sprite_height=100,200

text = pygame.font.Font(None, 27).render('This is a sprite ', True,
    pygame.Color('white'))
text_x=320
text_y=150

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    pygame.draw.rect(screen, sprite_col,(x, y, sprite_width, sprite_height))
    screen.blit(text,(text_x,text_y))
    pygame.display.flip()
    
pygame.quit()

