import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class Cube:
    # Class attribute
    rows = 0
    w = 0

    # Initialize instance attribute
    def __init__(self, start, dirnx=0, dirny=0, color=(255, 0, 0)):
        pass

    # Instance Method "move"
    def move(self, dirnx, dirny):
        pass

    # Instance Method "draw"
    def draw(self, surface, eyes=False):
        pass


class Snake:
    # Initialize instance attribute
    def __init__(self, color, position):
        pass

    # Instance Method "move"
    def move(self):
        pass

    # Instance Method "reset"
    def reset(self, pos):
        pass

    # Instance Method "addCube"
    def add_cube(self):
        pass

    # Instance Method "draw"
    def draw(self, surface):
        pass


def draw_grid(width, rows, surfae):



def redraw_window(surface):
    global rows, width, window
    # set screen color of window
    window.fill((0, 0, 0))
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snake(rows, items):
    pass


def message_box(subject, content):
    pass


# main loop
def main():
    global width, rows
    width = 500
    height = 500
    rows = 10
    # Create screen - width, height
    window = pygame.display.set_mode((width, height))
    # Snake object initiation
    s = Snake((255, 0, 0), (10, 10))
    # Control running
    running = True

    clock = pygame.time.Clock()
    while running:
        # pause the programme for an amount of time (millisecond) -> prevent from running to fast
        pygame.time.delay(50)
        # Frame rate limitation of 10
        clock.tick(10)

        redraw_window(window)


main()
