#!/usr/bin/python
# Ikke pille
import pygame
from setup_game import *

def setup():
    # Ting der skal ske naar spillet starter
    running = True

def loop():
    # Beregninger her
    pass

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
