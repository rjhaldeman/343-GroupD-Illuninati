import pygame
from Grid import *
from Card import *
from Deck import *
from Buttons import *


def homeScreen():
    # Initialize pygame
    pygame.init()

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Set the WIDTH and HEIGHT of the window
    screen = pygame.display.set_mode([700, 635])

    # Set title of screen
    pygame.display.set_caption("Home Screen")

    # Timer for blinking image
    elapsed_time = 0

    # Load images
    bg = pygame.image.load("Images/backgrounds/grungy_blue_texture_by_waitq.jpg")
    title_logo = pygame.image.load("Images/Illuminati Title Logo.jpg")
    title_logo = pygame.transform.scale(title_logo, (350, 450))  # resize
    start_button = pygame.image.load("Images/Start Button.png")
    start_button = pygame.transform.scale(start_button, (100, 100))  # resize

    while not done:
        # Increments timer for blinking image
        elapsed_time += clock.tick(30)

        # Background
        screen.blit(bg, (0, 0))

        # Illuminati Title Logo
        screen.blit(title_logo, (180, 40))

        # Blinking image
        if elapsed_time > 400:
            # Start Button
            startButton = screen.blit(start_button, (305, 510))
            if elapsed_time > 800:
                elapsed_time = 0

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
                pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()

                # If start button was clicked, return
                if startButton.collidepoint(pos):
                    pygame.event.get()
                    pygame.display.quit()
                    return

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'on exit.
    pygame.quit()


def mainScreen():
    # Uncontrolled Group Grid
    unControlled_grid = Grid()
    unControlled_grid.setSize(1, 10)
    unControlled_grid.setPosition([435, 10])

    # Controlled Group Grid
    grid = Grid()
    grid.setSize(7, 10)
    grid.setPosition([435, 115])

    # Special Card Grid
    special_grid = Grid()
    special_grid.setSize(1, 10)
    special_grid.setPosition([435, 574])

    # Buttons
    buttons = Buttons()

    # Deck
    deck = Deck()
    deck.loadCards("illuminati_cards.txt")
    deck.shuffle()
    deck.setPosition([1065, 270])

    # Discard Pile
    discard_pile = Deck()
    discard_pile.setPosition([1065, 460])

    # Initialize pygame
    pygame.init()

    # Loop until the user clicks the close button.
    done = False

    # Boolean for carrying any card
    carryingCard = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Set the WIDTH and HEIGHT of the window
    screen = pygame.display.set_mode([1280, 685])

    # Set title of screen
    pygame.display.set_caption("Main Screen")

    # Load images
    bg = pygame.image.load("Images/backgrounds/grungy_blue_texture_by_waitq.jpg")
    cg_label = pygame.image.load("Images/buttons/Grey/Controlled Groups.png")
    ucg_label = pygame.image.load("Images/buttons/Grey/Uncontrolled Groups.png")
    s_label = pygame.image.load("Images/buttons/Grey/Special Cards.png")
    d_label = pygame.image.load("Images/buttons/Grey/Deck small.png")
    dp_label = pygame.image.load("Images/buttons/Grey/Discard Pile small.png")
    i_logo = pygame.image.load("Images/Illuminati Logo.png")
    mb = pygame.image.load("Images/Message Box.png")
    itc_label_d = pygame.image.load("Images/Illuminati Title Card Label.png")
    itc_label_dp = pygame.image.load("Images/Illuminati Title Card Label.png")
    vcb = pygame.image.load("Images/View Card Box.png")

    while not done:
        # Background
        screen.blit(bg, (0, 0))

        # Illuminati Logo
        screen.blit(i_logo, (200, 20))

        # Message Box
        screen.blit(mb, (180, 260))

        # Grid Labels
        screen.blit(ucg_label, (440, 73))
        screen.blit(cg_label, (440, 532))
        screen.blit(s_label, (440, 637))

        # View Card Box
        screen.blit(vcb, (1040, 60))

        # Deck Labels
        screen.blit(d_label, (1070, 380))
        screen.blit(dp_label, (1070, 570))

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()

                if deck.wasClicked(pos):
                    drawnCard = deck.drawCard()

                    if drawnCard.cardType == 'special':
                        special_grid.add(drawnCard)
                    elif drawnCard.cardType == 'group':
                        unControlled_grid.add(drawnCard)
                    elif drawnCard.cardType == 'illuminati':
                        grid.add(drawnCard)

                # if not carrying a card
                if carryingCard is False:
                    for c in special_grid.card_list:
                        if c.wasClicked(pos) and carryingCard is False:
                            carryingCard = True
                            cardCurrentlyCarrying = c

                    for c in grid.card_list:
                        if c.wasClicked(pos) and carryingCard is False:
                            carryingCard = True
                            cardCurrentlyCarrying = c

                    for c in unControlled_grid.card_list:
                        if c.wasClicked(pos) and carryingCard is False:
                            carryingCard = True
                            cardCurrentlyCarrying = c

                # drop card
                else:
                    for c in special_grid.card_list:
                        if special_grid.wasClicked(pos):
                            # line up the card with the grid
                            adjusted_pos = special_grid.adjustedPosition(pos)
                            cardCurrentlyCarrying.setPosition(adjusted_pos)
                            carryingCard = False

                    for c in grid.card_list:
                        if grid.wasClicked(pos):
                            # line up the card with the grid
                            adjusted_pos = grid.adjustedPosition(pos)
                            cardCurrentlyCarrying.setPosition(adjusted_pos)
                            carryingCard = False

                    for c in unControlled_grid.card_list:
                        if unControlled_grid.wasClicked(pos):
                            # line up the card with the grid
                            adjusted_pos = unControlled_grid.adjustedPosition(pos)
                            cardCurrentlyCarrying.setPosition(adjusted_pos)
                            carryingCard = False

        # Get the current mouse position. This returns the position as a list of two numbers.
        player_position = pygame.mouse.get_pos()

        # which card am I carrying
        if carryingCard:
            cardCurrentlyCarrying.setPosition([player_position[0] - 5, player_position[1] - 5])

        # Draw the objects to screen

        # Left Panel
        buttons.drawMainMenu(screen)
        buttons.drawPlayerView(screen)

        # Middle Panel
        grid.drawTiles(screen)
        unControlled_grid.drawTiles(screen)
        special_grid.drawTiles(screen)

        # Right Panel
        deck.display(screen)
        discard_pile.display(screen)

        # update zoomed in view
        for c in grid.card_list:
            if c.isOverlaping(player_position):
                vcb = c.image

                # update zoomed in view
        for c in special_grid.card_list:
            if c.isOverlaping(player_position):
                vcb = c.image

                # update zoomed in view
        for c in unControlled_grid.card_list:
            if c.isOverlaping(player_position):
                vcb = c.image

                # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    pygame.quit()


def main():
    homeScreen()
    mainScreen()


main()