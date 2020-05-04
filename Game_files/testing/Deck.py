import pygame
import random
from Card import *
from constants import *

""" this class represents a group of cards """
""" examples: the main deck, discard_pile,..."""


class Deck(object):

    def __init__(self):
        """Setup variables in Deck class."""
        self.x = 100
        self.y = 100

        self.width = MEDIUM_CARD_WIDTH
        self.height = MEDIUM_CARD_HEIGHT

        self.card_count = 0
        self.card_list = []

        self.topImage = pygame.image.load("Images/Illuminati Title Card Label.png")
        self.emptyDeckImage = pygame.image.load("Images/Illuminati Title Card Label Null.png")
        # scale down to normal size
        self.topImage = pygame.transform.scale(self.topImage, (self.width, self.height))
        self.emptyDeckImage = pygame.transform.scale(self.emptyDeckImage, (self.width, self.height))

    # load cards from file
    def loadCards(self, file_name):
        file = open(file_name, "r")
        for line in file:
            if line[0] != '#':
                # print(line)
                card = Card()
                card.loadFromFile(line)
                self.addCard(card)

    # add a card to the bottom of the deck
    def addCard(self, Card):
        self.card_list.append(Card)
        self.card_count += 1

    # take top card out of deck
    def drawCard(self):
        # if deck is not empty
        if len(self.card_list) != 0:
            self.card_count -= 1
            return self.card_list.pop(0)

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.card_list)

    # display the deck on screen
    def display(self, screen):
        if len(self.card_list) > 0:
            screen.blit(self.topImage, [self.x, self.y])
        else:
            screen.blit(self.emptyDeckImage, [self.x, self.y])

    # set the position of the deck
    def setPosition(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    # repositions the object to be next to the right edge position of the given screen
    def rightPosition(self, screen_width, offset):
        self.x = int(screen_width - self.width + offset)

    # print("new deck.x:", self.x)

    # repositions the object to be next to the bottom edge position of the given screen
    def bottomPosition(self, screen_height, offset):
        self.y = int(screen_height - self.height + offset)

    # print("new deck.y:", self.y)

    # repositions the object to be next to the bottom edge position of the given screen
    def bottomRightPosition(self, window_size, offset):
        # print("new deck position: ")
        self.bottomPosition(window_size[1], offset[1])
        self.rightPosition(window_size[0], offset[0])

    def wasClicked(self, pos):
        if pos[0] - self.x > 0 and pos[0] - self.x < self.width:
            if pos[1] - self.y > 0 and pos[1] - self.y < self.height:
                # print("Card Click ", pos)
                return True
        return False