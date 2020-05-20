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
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color


    # Instance Method "move"
    def move(self, dirnx, dirny):
        pass

    # Instance Method "draw"
    def draw(self, surface, eyes=False):
        pass


class Snake:
    # List of cubes = snake body
    body = []
    # dictionary of turns
    turns = {}

    # Initialize instance attribute
    def __init__(self, color, position):
        self.color = color
        # head = cube object -> made out of cube object
        self.head = Cube(position)
        self.body.append(self.head)
        # Direction for x (only one direction moving)
        self.dirnx = 0
        # Direction for y
        self.dirny = 1

    # Instance Method "move"
    def move(self):
        # Get a dictionary of keys getting pressed
        keys = pygame.key.get_pressed()

        for key in keys:
            # elif prevent more than one key pressing

            if keys[pygame.K_LEFT]:
                self.dirnx = -1
                # prevent diagonal move
                self.dirny = 0
                # save turns so that the whole body can make a turn
                self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_RIGHT]:
                self.dirnx = 1
                # prevent diagonal move
                self.dirny = 0
                # save turns so that the whole body can make a turn
                self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_UP]:
                self.dirny = -1
                # prevent diagnoal move
                self.dirnx = 0
                # save turns so that the whole body can make a turn
                self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_DOWN]:
                self.dirny = 1
                # prevent diagnoal move
                self.dirnx = 0
                # save turns so that the whole body can make a turn
                self.turns[self.head.position[:]] = [self.dirnx, self.dirny]

        # Moving Cube (enumerate = keep count of the iteration)
        # i = index, c = cube
        for i, c in enumerate(self.body):
            # [:] = copy -> each of cube (body) has position -> get their position
            p = c.position[:]
            # check if the position in turn list
            if p in self.turns:
                # get turn information
                turn = self.turns[p]
                # move cube method
                c.move(turn[0], turn[1])
                # if last cube = remove from the list, nex time, making wrong turn
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                # boundary checking
                # Left
                if c.dirnx == -1 and c.position[0] <= 0:
                    c.position = (c.rows - 1, c.position[1])
                # Right
                elif c.dirnx == 1 and c.position[0] >= c.rows - 1:
                    c.position = (0, c.position[1])
                # Bottom
                elif c.dirny == 1 and c.position[1] >= c.rows - 1:
                    c.position = (c.position[0], 0)
                # Top
                elif c.dirny == -1 and c.position[1] <= 0:
                    c.position = (c.position[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    # Instance Method "reset"
    def reset(self, pos):
        pass

    # Instance Method "addCube"
    def add_cube(self):
        pass

    # Instance Method "draw"
    def draw(self, surface):
        for index, cube in enumerate(self.body):
            if index == 0:
                # head
                cube.draw(surface, True)
            else:
                cube.draw(surface)


def draw_grid(widt, row, windo):
    # Determining each cube size
    size_btwen = width // row
    x = 0
    y = 0
    for i in range(rows):
        x += size_btwen
        y += size_btwen

        # draw vertical line
        pygame.draw.line(windo, (255, 255, 255), (x, 0), (x, widt))

        # draw horizontal line
        pygame.draw.line(windo, (255, 255, 255), (0, y), (widt, y))


def redraw_window(windo):
    global rows, width, snake
    snake.draw(windo)
    draw_grid(width, rows, windo)
    pygame.display.update()


def random_snake(rows, items):
    pass


def message_box(subject, content):
    pass


# main loop
def main():
    global width, rows, snake
    width = 500
    height = 500
    rows = 10
    # Create screen - width, height
    window = pygame.display.set_mode((width, height))

    # set screen color to black
    window.fill((0, 0, 0))

    # Control running
    running = True

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # keystroke testing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        snake = Snake((255, 0, 0), (10, 10))
        # pause the programme for an amount of time (millisecond) -> prevent from running to fast
        pygame.time.delay(50)
        # Frame rate limitation of 10
        clock.tick(10)

        redraw_window(window)


main()
