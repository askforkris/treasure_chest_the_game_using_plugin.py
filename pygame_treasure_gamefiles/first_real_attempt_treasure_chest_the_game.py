import pygame
from pygame import display

# game variables
one_coin = [5]
gold_coin = [25]
silver_coin = [4]
pygame.display.set_caption('treasure!')
fps = 60
timer = pygame.time.Clock()
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
results = ['Player WINS!, Player lose']

display.set_mode()
width = 400
length = 500
# Initializing surface
# set the pygame window name
scrn = pygame.display.set_caption("Treasure_chest")
# create a surface object, image is drawn on it.

imp = pygame.image.load("C:\\Users\\askforkris\\Downloads\\Chest_set1\\chest_set.png")

scrn.blit(imp), (0, 0)

# Initializing RGB Color
color = (255, 255, 255)

# initializing imported module
pygame.init()

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


def deal_coins(current_hand, current_deck, current_coin=5, ):
    coin = random.randint(1, 26)
    return current_hand, current_coin
    if Lucky_number == '25':
        coin == vars("25 == x")
        one_coin = x = ('try_another_coin')
        silver_coin = randon.randit(1, 6)
        gold_coin = ('25')
        if player_score == ('25'):
            ('player_wins')

            import random.randit
            def guess():
                comp_guess = (random.randit(1, 6, 25))
