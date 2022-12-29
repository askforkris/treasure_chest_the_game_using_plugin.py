# treasure_chest_the_game_using_plugin.py
THis is my second attempt of gettting some where with my game. My only question is how do I get the display window to stay open . I"m using pygame. I"m becoming familiar with the terminalogy. how will it look when displayed 
import copy
import os
import random
import pygame
from pygame.surface import Surface, SurfaceType

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( "First Game!" )



WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()
# game variables
one_coin = [5]
gold_coin = [25]
silver_coin = [4]
pygame.display.set_caption( 'Pygame Blackjack!' )
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font( 'freesansbold.ttf', 44 )
smaller_font = pygame.font.Font( 'freesansbold.ttf', 36 )
active = False
# win, loss,
records = [0, 0, 0]
player_score = 0
initial_deal = False
my_hand = []
outcome = 0
hand_active = False
outcome = 0
add_score = False
results = [, 'Player WINS!, Player lose:)

chest_set_image = pygame.image.load(
    os.path.join('assets', 'chest_set.png' ))

# coins by selecting randomly from chest, and make function for one card at a time
def deal_coins ( current_hand, current_deck, current_coin=5, ):
    coin = random.randint( 1, 26 )
    return current_hand, current_coin
    if Lucky_number == '25':
        coin == vars( "25 == x" )
        one_coin = x = ('try_another_coin')
        silver_coin = randon.randit(1,6)
        gold_coin = ('25')
        if player_score == ('25'):
            ('player_wins')

            import random.randit
            def guess():
                    comp_guess = (random.randit(1,6,25))


