# activate the pygame library
import pygame
import sys

pygame.init()
FPS = 30
fpsClock = pygame.time.Clock()
# set up window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Treasure_chest')
WHITE = (255, 255, 255)
chest2_image = pygame.image.load('chest_set2.png')
pygame.image.load('chest_set2.png')
chestx = 10
chesty = 10
while True:  # the main game loop
    DISPLAYSURF.fill(WHITE)


# game variables
# Gold_coin = 25
# silver_coin = 5
# loser = '>25'
# winner = '<25'
# current_draw = 'deal_coins'
# current_play = 'treasure_pot'
def computer_out_put(game_values, winner_vaules):
    if "player_score" != '25':
        return "Gold_coin_winner"

        DISPLAYSURF.blit(chestImg, (chestx, chesty))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()
                fpsClock.tick(FPS)
