import pygame
from constants import *

""" this class represents the players card space """


class Grid(object):

    def __init__(self):
        """ Setup variables in Grid class. """

        """ width & height of each square """
        self.width = SMALL_CARD_WIDTH
        self.height = SMALL_CARD_WIDTH
        self.margin = 5

        """Rows and Columns"""
        # self.size
        self.rows = 9
        self.cols = 9

        """Grid Position"""
        self.x = (WINDOW_SIZE[0] / 2) - (self.width * self.rows / 2)
        self.y = 100

        # color of each tile
        self.color = WHITE

        self.tileImage = pygame.image.load("Images/60x60tile.png")

        self.tileImage = pygame.transform.scale(self.tileImage, (self.width, self.height))

        # def initGrid(self):
        # self.grid keeps track of occupied positions
        self.grid = []
        for row in range(self.rows):
            # Add empty array
            self.grid.append([])
            for column in range(self.cols):
                # Append a Card-> 0 for test example
                self.grid[row].append(0);

        self.grid[4][4] = 1
        self.card_list = []
        self.power = 2

    # --- Methods ---#

    # Sets the number of rows and columns of the grid
    def setSize(self, r, c):
        self.rows = r
        self.cols = c
        del self.grid[:]
        self.initGrid()

    # sets the position to the given values
    # pos is a tupple, two values in one
    def setPosition(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    # Aligns object to the horizontal center
    def centerXposition(self, window_size):
        grid_width = (self.width + self.margin) * self.cols
        self.x = int((window_size[0] - grid_width) / 2)
        print("new grid.x:", self.x)

    # Aligns object to the vertical center
    def centerYposition(self, window_size):
        grid_height = (self.height + self.margin) * self.rows
        self.y = int((window_size[1] - grid_height) / 2)
        print("new grid.y:", self.y)

    # Aligns objcect to the center of the screen
    def centerPosition(self, window_size):
        self.centerXposition(window_size)
        self.centerYposition(window_size)

    # initiates grid variable
    def initGrid(self):
        for row in range(self.rows):
            # Add empty array
            self.grid.append([])
            for column in range(self.cols):
                # Append a Card-> 0 for test example
                self.grid[row].append(0);

    # translates a pixel position to the nearest tile position
    def adjustedPosition(self, pos):
        # The adjusted position depends on the cards orientation
        # for now this method works only for horizontal orientation
        column = (pos[0] - self.x) // (self.width + self.margin)
        row = (pos[1] - self.y) // (self.height + self.margin)
        x = self.x + column * (self.width + self.margin) + self.margin
        y = self.y + row * (self.height + self.margin) + self.margin + 10  # 10 for horizontal orientation
        return [x, y]

    # testing not done!!!
    # translates a tile position to pixel position
    def tileToPixelPosition(self, pos):
        # The adjusted position depends on the cards orientation
        # for now this method works only for horizontal orientation
        x = self.x + pos[1] * (self.width + self.margin) + self.margin
        y = self.y + pos[0] * (self.height + self.margin) + self.margin + 10  # 10 for horizontal orientation
        return [x, y]

    # returns true if the grid area was clicked
    def wasClicked(self, pos):
        if pos[0] - self.x > 0 and pos[0] - self.x < (self.width + self.margin) * self.cols:
            if pos[1] - self.y > 0 and pos[1] - self.y < (self.height + self.margin) * self.rows:
                return True
        return False

    # changes the clicked grid position to occupied
    def click(self, pos):
        # Change the x y screen coordinates to grid coordinates
        column = (pos[0] - self.x) // (self.width + self.margin)
        row = (pos[1] - self.y) // (self.height + self.margin)

        if self.wasClicked(pos):
            # set location to one
            print("Grid Click ", pos, "coordinates: ", int(row), int(column))
            self.grid[int(row)][int(column)] = 1;

    # alternative to drawTiles() use one or the other
    # this version prints the tiles with the specified color self.color
    def draw(self, screen):
        for row in range(self.rows):
            for column in range(self.cols):
                color = self.color
                if self.grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(self.margin + self.width) * column + self.margin + self.x,
                                  (self.margin + self.height) * row + self.margin + self.y,
                                  self.width,
                                  self.height])
        self.displayCards(screen)

    # alternative to draw() use one or the other
    # this version prints the self.image at each tile position
    def drawTiles(self, screen):
        for row in range(self.rows):
            for column in range(self.cols):
                x_pos = (self.margin + self.width) * column + self.margin + self.x
                y_pos = (self.margin + self.height) * row + self.margin + self.y
                pos = [x_pos, y_pos]
                screen.blit(self.tileImage, pos)
        self.displayCards(screen)

    def displayCards(self, screen):
        for c in self.card_list:
            c.draw(screen)

    # adds a card to the grid
    def add(self, card):
        # check if card is null
        if card is not None:
            pos = self.getNextEmptyPosition()
            # print("empty position (coord): " , pos)

            self.grid[pos[0]][pos[1]] = 1

            pos = self.tileToPixelPosition(pos)
            # print("empty position (pixel): " , pos)
            # print("")

            card.setPosition(pos)
            self.card_list.append(card)

    # returns the tile position of the first empty space
    def getNextEmptyPosition(self):
        # pos = [0,0]
        for row in range(self.rows):
            for column in range(self.cols):
                if self.grid[row][column] == 0:
                    return [row, column]
