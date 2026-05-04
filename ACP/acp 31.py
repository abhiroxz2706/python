import pygame

pygame.init()
screen_width,screen_height=500,500
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Moving rectangular sprite")

sprite_col=pygame.Color("lightblue")
x,y = 77,77
sprite_width,sprite_height=77,12


clock=pygame.time.Clock()

done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

           
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x-=3
    if pressed[pygame.K_RIGHT]: x+=3
    if pressed[pygame.K_UP]: y+=3
    if pressed[pygame.K_DOWN]: y-=3

    x = min(max(0, x), screen_width - sprite_width)
    y = min(max(0, y), screen_height - sprite_height)
    
    
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, sprite_col,(x, y, sprite_width, sprite_height))
    pygame.display.flip()
    clock.tick(200)