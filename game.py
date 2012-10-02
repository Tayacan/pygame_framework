#!/usr/bin/python
# Ikke pille
import pygame
from setup_game import *

def setup():
    # Ting der skal ske naar spillet starter
    pass

def loop():
    # Beregninger her
    pass

def events():
    # Events, for eksempel tastetryk.
    # pygame.QUIT er naar man trykker paa
    # luk-knappen.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop()
