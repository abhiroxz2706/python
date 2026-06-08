import pygame
import sys

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Screen setup
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Sound Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)

# Load sound
# Replace "sound.wav" with your sound file
sound = pygame.mixer.Sound("sound.wav")

# Circle position
x = WIDTH // 2
y = HEIGHT // 2

# Game loop
running = True

while running:
    screen.fill(WHITE)

    # Draw circle
    pygame.draw.circle(screen, BLUE, (x, y), 40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Play sound when SPACE key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound.play()

    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()