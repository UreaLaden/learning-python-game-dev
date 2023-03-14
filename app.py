import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("Space Shooter X")
screen = pygame.display.set_mode((480,600))

while True:
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            #This is a bad piece of code
            exit()
    
    pygame.time.Clock().tick(60)