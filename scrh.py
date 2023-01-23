# activate the pygame library
import pygame

pygame.init()
FPS = 60
surface = pygame.display.set_mode((680, 480))
# initializing RGB color
color = (0, 0, 0, 0.0)
# changing surface color
surface.fill(color)
pygame.display.flip()
pygame.display.set_caption('Treasure_chest')
# initializing surface image
pygame.init()
imp = pygame.image.load('images/olchest.png').convert()
# initializing surface blit
surface.blit(imp, (226, 160))
# paint screen one time
pygame.display.flip()
# initializing exit
status = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.init()
            pygame.quit()
            exit()
pygame.display.update()
