#!/usr/bin/python
import pygame
import setup_game
import game

def main ():
    pygame.init()
    size = (800,600)

    game.setup()
    while True:
        game.events()
        game.loop()
        pygame.display.flip()

if __name__ == "__main__":
    main()
