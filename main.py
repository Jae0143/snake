import random
import pygame

# initalize pygame
pygame.init()


class Cube:
    # Class attribute
    rows = 20
    w = 500

    # Initialize instance attribute
    def __init__(self, start, dirnx=0, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    # Instance Method "move"
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    # Instance Method "draw"
    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        row_cor = self.pos[0]
        colum_cor = self.pos[1]

        # Draw (row_cor * dis, colum_cor * dis) -> (x,y, width, height)
        pygame.draw.rect(surface, self.color, (row_cor * dis + 1, colum_cor * dis + 1, dis - 2, dis - 2))

        # draw eyes on the head
        if eyes:
            # find middle
            center = dis // 2
            # eye radius
            radius = 3
            # Eyes coordination
            eye_1 = (row_cor * dis + 20, colum_cor * dis + 8)
            eye_2 = (row_cor * dis + 10, colum_cor * dis + 8)

            # draw eyes
            pygame.draw.circle(surface, (0, 0, 0), eye_1, radius)
            pygame.draw.circle(surface, (0, 0, 0), eye_2, radius)


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
        # dictionary of pressed key
        keys = pygame.key.get_pressed()

        for key in keys:
            # elif prevent more than one key pressing
            if keys[pygame.K_LEFT]:

                self.dirnx = -1
                # prevent diagonal move
                self.dirny = 0
                # save turns so that the whole body can make a turn
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_RIGHT]:

                self.dirnx = 1
                # prevent diagonal move
                self.dirny = 0
                # save turns so that the whole body can make a turn
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_UP]:

                self.dirny = -1
                # prevent diagnoal move
                self.dirnx = 0
                # save turns so that the whole body can make a turn
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            elif keys[pygame.K_DOWN]:

                self.dirny = 1
                # prevent diagnoal move
                self.dirnx = 0
                # save turns so that the whole body can make a turn
                self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # Moving Cube (enumerate = keep count of the iteration)
        # i = index, c = cube
        for i, c in enumerate(self.body):
            # [:] = copy -> each of cube (body) has position -> get their position
            p = c.pos[:]
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
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                # Right
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                # Bottom
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                # Top
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    # Instance Method "reset"
    def reset(self, position):
        # reset everything to default
        self.head = Cube(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    # Instance Method "addCube"
    def add_cube(self):
        # last one in body
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
        # add cube depending on the direction of snake moving
        # moving right -> add at the left
        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        # Moving left
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        # Moving down
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        # Moving up
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        # Make the moving direction equal to the rest of the body
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    # Instance Method "draw"
    def draw(self, surface):
        for index, cub in enumerate(self.body):
            if index == 0:
                # head
                cub.draw(surface, True)
            else:
                cub.draw(surface)


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


def random_snack(rows, snake):
    positions = snake.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        # length of filtered list and make sure that snack is not on same position as snack -> skip it
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def message_box(windo, score):
    over_font = pygame.font.Font('ARCADECLASSIC.TTF', 100)
    over_font_2 = pygame.font.Font('ARCADECLASSIC.TTF', 50)
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    over_text_2 = over_font_2.render("Your Score  {}".format(score), True, (255, 255, 255))
    windo.blit(over_text, (25, 150))
    windo.blit(over_text_2, (100, 250))


# main loop
def main():
    global width, rows
    over = False
    width = 500
    height = 500
    rows = 20
    # Create screen - width, height
    window = pygame.display.set_mode((width, height))

    # Title and Icon
    pygame.display.set_caption("Snake")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

    # Control running
    running = True

    # Snake Object
    snakee = Snake((255, 0, 0), (5, 5))

    # Snack object
    snack = Cube(random_snack(rows, snakee), color=(0, 255, 0))

    clock = pygame.time.Clock()

    keys = pygame.key.get_pressed()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # keystroke testing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # pause the programme for an amount of time (millisecond) -> prevent from running to fast
        pygame.time.delay(50)
        # Frame rate limitation of 10
        clock.tick(100)

        # set screen color to black
        window.fill((0, 0, 0))

        # draw grid
        draw_grid(width, rows, window)

        # Draw snack
        snack.draw(window)

        # check collision and generate new snack
        if snakee.body[0].pos == snack.pos:
            # Increase the length
            snakee.add_cube()
            # generate new snack
            snack = Cube(random_snack(rows, snakee), color=(0, 255, 0))

        # Draw snake
        snakee.draw(window)

        # move snake
        snakee.move()

        # Check the collision between snake body -> game over
        for index_cube in range(len(snakee.body)):

            # checking if current index_cube's position is in any of the other cube's position
            if snakee.body[index_cube].pos in list(map(lambda z: z.pos, snakee.body[index_cube + 1:])):
                over = True
                break
        if over:
            window.fill((0, 0, 0))
            message_box(window, len(snakee.body))

        # make snake constantly moving and cheking for key press
        pygame.display.update()


main()
