import pygame
from constants import *


class Card(object):
    """ Static variables in Card class. """
    TitleCardImage = pygame.image.load("Images/Illuminati_Tittle_Card.png")
    TitleCardMiniImage = pygame.image.load("Images/Illuminati_Tittle_Card60x40.png")
    TitleCardMiniRotatedImage = pygame.image.load("Images/Illuminati_Tittle_Card60x40r.png")
    HORIZONTAL = 0
    VERTICAL = 1

    def __init__(self):
        self.image = Card.TitleCardImage
        self.miniImage = Card.TitleCardMiniImage
        self.miniImageRotated = Card.TitleCardMiniRotatedImage

        # Width & Height of card
        self.width = SMALL_CARD_WIDTH
        self.height = SMALL_CARD_HEIGHT

        """Screen Position && Orientation"""
        self.x = 0
        self.y = 0
        orientation = Card.HORIZONTAL

        self.faceUp = True
        self.direction = "up"

        # values loaded from file
        self.name = "card name:"
        self.specialAbility = "card ability"
        self.cardType = "none"

        self.directPower = 0
        self.supportPower = 0
        self.resistance = 0
        self.income = 0

        self.alignment1 = "none"
        self.alignment2 = "none"
        self.alignment3 = "none"

        # default arrow type = o (out)
        self.arrowuP = "o"
        self.arrowuDown = "o"
        self.arrowLeft = "o"
        self.arrowRight = "o"

        # values updated during gameplay
        self.megaBucks = 0

        # scale images
        self.image = pygame.transform.scale(self.image, (LARGE_CARD_WIDTH, LARGE_CARD_HEIGHT))

    # rotate images

    def loadFromFile(self, line):
        parts_list = line.split(' / ')
        for s in parts_list:
            s = s.strip()
        # print("[" + s + "]")

        self.directPower = parts_list[0]
        self.supportPower = parts_list[1]
        self.resistance = parts_list[2]
        self.income = parts_list[3]

        self.alignment1 = parts_list[4]
        self.alignment1 = parts_list[5]
        self.alignment1 = parts_list[6]

        self.arrowuP = parts_list[7][0]
        self.arrowuDown = parts_list[7][1]
        self.arrowLeft = parts_list[7][2]
        self.arrowRight = parts_list[7][3]

        self.name = parts_list[8].strip()
        image_file_name = "Images/cards/" + self.name + ".png"
        self.loadImage(image_file_name)

        self.cardType = parts_list[9].strip()

    # --- Methods ---
    def flip(self):
        if self.faceUp:
            self.faceUp = False
        else:
            self.faceUp = True

    def collectIncome(self):
        self.megaBucks += self.income

    # def displayMini(self, screen):
    def draw(self, screen):

        screen.blit(self.miniImage, [self.x, self.y])

    def displayLarge(self, screen):
        screen.blit(self.image, [self.x, self.y])

    def loadImage(self, image_file_name):
        # load
        self.image = pygame.image.load(image_file_name)
        # scale down to mini size
        self.miniImage = pygame.transform.scale(self.image, (SMALL_CARD_WIDTH, SMALL_CARD_HEIGHT))
        # rotate mini image by 90 degrees
        self.miniImageRotated = pygame.transform.rotate(self.image, 90)
        # scale original to zoom in size
        self.image = pygame.transform.scale(self.image, (LARGE_CARD_WIDTH, LARGE_CARD_HEIGHT))

    def getImage(self):
        return self.image

    def setImage(image):
        self.image = image

    def setPosition(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    """ 
    #can not overload in python as in C++ or JAVA
    def setPosition(self, x, y):
        self.x = x
        self.y = y
    """

    # repositions the object to be next to the right edge position of the given screen
    def rightPosition(self, screen_width, offset):
        self.x = int(screen_width - self.width + offset)

    # repositions the object to be next to the bottom edge position of the given screen
    def topPosition(self, screen_height, offset):
        self.y = int(offset)

    # repositions the object to be next to the bottom edge position of the given screen
    def topRightPosition(self, window_size, offset):
        self.topPosition(window_size[1], offset[1])
        self.rightPosition(window_size[0], offset[0])

    def wasClicked(self, pos):
        if pos[0] - self.x > 0 and pos[0] - self.x < self.width:
            if pos[1] - self.y > 0 and pos[1] - self.y < self.height:
                return True
        return False

    def isOverlaping(self, pos):
        return self.wasClicked(pos)

