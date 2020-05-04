import pygame
from constants import *


class Buttons(object):

    def __init__(self):
        # Load Buttons & Labels

        # Players
        self.view = pygame.image.load('Images/buttons/Yellow/View 200x50.png')
        self.view = pygame.transform.scale(self.view, (150, 40))  # resize
        self.player1 = pygame.image.load('Images/buttons/Grey/P1.png')
        self.player1 = pygame.transform.scale(self.player1, (37, 37))  # resize
        self.player2 = pygame.image.load('Images/buttons/Grey/P2.png')
        self.player2 = pygame.transform.scale(self.player2, (37, 37))  # resize
        self.player3 = pygame.image.load('Images/buttons/Grey/P3.png')
        self.player3 = pygame.transform.scale(self.player3, (37, 37))  # resize
        self.player4 = pygame.image.load('Images/buttons/Grey/P4.png')
        self.player4 = pygame.transform.scale(self.player4, (37, 37))  # resize

        # Regular Actions
        self.main_menu = pygame.image.load('Images/buttons/Yellow/Main Menu.png')
        self.main_menu = pygame.transform.scale(self.main_menu, (150, 40))  # resize
        self.reg_actions = pygame.image.load('Images/buttons/Grey/Regular Actions.png')
        self.reg_actions = pygame.transform.scale(self.reg_actions, (150, 40))  # resize
        self.attackButton = pygame.image.load('Images/buttons/Grey/attack.png')
        self.attackButton = pygame.transform.scale(self.attackButton, (150, 40))  # resize
        self.transfermoney = pygame.image.load('Images/buttons/Grey/transfer_money.png')
        self.transfermoney = pygame.transform.scale(self.transfermoney, (150, 40))  # resize
        self.movegroup = pygame.image.load('Images/buttons/Grey/move_group.png')
        self.movegroup = pygame.transform.scale(self.movegroup, (150, 40))  # resize

        # Free Actions
        self.free_actions = pygame.image.load('Images/buttons/Grey/Free Actions.png')
        self.free_actions = pygame.transform.scale(self.free_actions, (150, 40))  # resize
        self.dropGroup = pygame.image.load('Images/buttons/Grey/drop_group.png')
        self.dropGroup = pygame.transform.scale(self.dropGroup, (150, 40))  # resize
        self.give_away_money = pygame.image.load('Images/buttons/Grey/give_away_money.png')
        self.give_away_money = pygame.transform.scale(self.give_away_money, (150, 40))  # resize
        self.useSpecial = pygame.image.load('Images/buttons/Grey/use_special.png')
        self.useSpecial = pygame.transform.scale(self.useSpecial, (150, 40))  # resize

        # Given Actions
        self.given_actions = pygame.image.load('Images/buttons/Grey/Given Actions.png')
        self.given_actions = pygame.transform.scale(self.given_actions, (150, 40))  # resize
        self.transfermoney2 = pygame.image.load('Images/buttons/Grey/transfer_money.png')
        self.transfermoney2 = pygame.transform.scale(self.transfermoney2, (150, 40))  # resize
        self.specialPower = pygame.image.load('Images/buttons/Grey/special_power.png')
        self.specialPower = pygame.transform.scale(self.specialPower, (150, 40))  # resize
        self.passTurn = pygame.image.load('Images/buttons/Grey/pass.png')
        self.passTurn = pygame.transform.scale(self.passTurn, (150, 40))  # resize

        # Position
        self.x = 10
        self.y = 30

    def drawPlayerView(self, screen):
        # Draw Buttons & Labels

        # Players
        screen.blit(self.view, [self.x, self.y])
        screen.blit(self.player1, [self.x, self.y + 40])
        screen.blit(self.player2, [self.x + 38, self.y + 40])
        screen.blit(self.player3, [self.x + 76, self.y + 40])
        screen.blit(self.player4, [self.x + 114, self.y + 40])

    def drawMainMenu(self, screen):
        # Draw Buttons & Labels

        # Regular Actions
        screen.blit(self.main_menu, [self.x, self.y + 100])
        screen.blit(self.reg_actions, [self.x, self.y + 140])
        screen.blit(self.attackButton, [self.x, self.y + 180])
        screen.blit(self.transfermoney, [self.x, self.y + 220])
        screen.blit(self.movegroup, [self.x, self.y + 260])

        # Free Actions
        screen.blit(self.free_actions, [self.x, self.y + 300])
        screen.blit(self.dropGroup, [self.x, self.y + 340])
        screen.blit(self.give_away_money, [self.x, self.y + 380])
        screen.blit(self.useSpecial, [self.x, self.y + 420])

        # Given Actions
        screen.blit(self.given_actions, [self.x, self.y + 460])
        screen.blit(self.transfermoney2, [self.x, self.y + 500])
        screen.blit(self.specialPower, [self.x, self.y + 540])
        screen.blit(self.passTurn, [self.x, self.y + 580])