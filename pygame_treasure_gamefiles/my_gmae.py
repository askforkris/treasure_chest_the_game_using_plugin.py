import os
import random

import pygame

pygame.font.init()
pygame.mixer.init()

# import pygame package
import pygame

# initializing imported module
pygame.init()

# displaying a window of height
# 500 and width 400
pygame.display.set_mode((400, 500))

# creating a bool value which checks
# if game is running
running = True

# keep game running till running is true
while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False

# game variables
silver_coin = [5]
gold_coin = [25]
silver_coin = [4]
pygame.display.set_caption('Treasure_Chest_the_game!')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 44)
smaller_font = pygame.font.Font('freesansbold.ttf', 36)
active = False
# win, loss,
records = [0, 0, 0]
player_score = 0
initial_deal = False
my_hand = []
outcome = 0
hand_active = False
outcome = 0
add_score: bool = False
results = ['', 'PLAYER BUSTED o_O', 'Player WINS! :)', 'DEALER WINS :(', 'TIE GAME...']

chest_set_image = pygame.image.load(
    os.path.join('../assets', 'Treasure_chest_set.png'))


# coins by selecting randomly from chest, and make function for one card at a time
class Lucky_number:
    pass


def deal_coins(current_hand, current_deck, current_coin=5, ):
    coin = random.randint(1, 5, 26)
    return current_hand, current_coin

    def computer_out_put(game_values, ):
        if Lucky_number != '25':
            return gold_coin

    gold_coin == vars("25 == x")
    silver_coin == random.randit(1, 6)

    def fuction(Adding_values_game_logic):

        silver_coin = randon.randit(1, 6)
    return

    def fcuntion(five_coins_Game_math, five_silver_coins=player_score):
        vars("25 == winner")
        vars(">25 == loser")
