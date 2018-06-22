"""
Pong game in python, using pygame
original code taken from: https://codereview.stackexchange.com/questions/33289/basic-pong-game-in-pygame
adapted for two-player game with pihut gamepads (keyboard handling commented out)

Details:
    - (0,0) in upper left corner, x increases rightwards, y increases downwards
    - items marked as 'not important' are in regards to adapting for CM matrix

PiHut Gamepad keys w/ pygame:
    - Directions cross:
        * pygame.JOYAXISMOTION
        * Pressing button:
            * Up and Down:
                - event.axis = 1
                * Up: event.value = -1.0000305...
                * Down: event.value = 1.0
            * Left and Right:
                - event.axis = 0
                * Left: event.value = -1.0000305...
                * Right: event.value = 1.0
        * Releasing button:
            - event.value = 0
            - event.axis remains as above
    - Buttons:
        * Pressing: pygame.JOYBUTTONDOWN
        * Releasing: pygame.JOYBUTTONUP
        - X: event.button = 0
        - A: event.button = 1
        - B: event.button = 2
        - Y: event.button = 3
        - L: event.button = 4
        - R: event.button = 5
        - Select: event.button = 8
        - Start: event.button = 9
    (nobody knows what happened to 6 and 7...)
"""


import pygame
import sys
from random import randint


class Ball(object):
    def __init__(self, x, y, width, height, x_change, y_change, colour):
        self.x = x
        self.y = y
        self.width = width                      # not important
        self.height = height                    # not important
        self.x_change = x_change
        self.y_change = y_change
        self.speed = 1
        self.colour = colour

    def render(self, screen):                   # not important
        pygame.draw.ellipse(screen, self.colour, self.rect)

    def accelerate(self):
        if self.speed < 3:
            self.speed += 0.2

    def update(self):
        self.x += self.x_change * self.speed
        self.y += self.y_change * self.speed

    @property
    def rect(self):                             # not important
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Paddle(object):
    def __init__(self, x, y, width, height, speed, screen_height, colour):
        self.x = x
        self.y = y
        self.width = width                      # not important
        self.height = height
        self.y_change = 0
        self.speed = speed
        self.screen_height = screen_height
        self.colour = colour                    # not important

    def render(self, screen):                   # not important
        pygame.draw.rect(screen, self.colour, self.rect)

    def update(self):
        if self.y < 0:
            self.y = 0
        elif (self.y + self.height) > self.screen_height:
            self.y = self.screen_height - self.height
        else:
            self.y += self.y_change

    def key_handler(self, event):
        if event.value <= -1 and self.y > 0:                                    # UP
            self.y_change = -self.speed
        elif event.value >= 1 and (self.y + self.height) < self.screen_height:  # DOWN
            self.y_change = self.speed
        else:
            self.y_change = 0

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP and self.y > 0:
        #         self.y_change = -self.speed
        #     elif event.key == pygame.K_DOWN and (self.y + self.height) < self.screen_height:
        #         self.y_change = self.speed
        # elif event.key in (pygame.K_UP, pygame.K_DOWN):
        #     self.y_change = 0

    @property
    def rect(self):                             # not important
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Pong(object):
    COLOURS = {"BLACK":   (0,   0,   0),
               "WHITE": (255, 255, 255), }

    def __init__(self):
        pygame.init()
        for _ in range(pygame.joystick.get_count()):
            pygame.joystick.Joystick(_).init()
        WIDTH, HEIGHT = 200, 100
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # not important
        pygame.display.set_caption("Lewis' Adapted Pong")       # not important
        self.clock = pygame.time.Clock()
        ball_x = randint(80, 120)
        ball_y = randint(40, 60)
        self.ball = Ball(ball_x, ball_y, 10, 10, 1, 1, Pong.COLOURS["BLACK"])
        self.player1 = Paddle(10, HEIGHT/2 - 10,  10, (HEIGHT * 30)/HEIGHT,
                              1, HEIGHT, Pong.COLOURS["BLACK"])
        self.player2 = Paddle(WIDTH - 20, HEIGHT/2 - 10,  10, (HEIGHT * 30)/HEIGHT,
                              1, HEIGHT, Pong.COLOURS["BLACK"])
#        self.score = 0

    def pause(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                    self.play()
            pygame.display.update()
            clock.tick(15)

    def play(self):
        pygame.time.set_timer(1, 5000)
        while True:
            self.clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                    self.pause()
                if event.type == pygame.JOYAXISMOTION and event.axis == 1:
                    if event.joy == 0:
                        self.player1.key_handler(event)
                    # elif event.joy == 1:
                        self.player2.key_handler(event)
                # if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                #    self.player1.key_handler(event)
                #    self.player2.key_handler(event)
                if event.type == 1:
                    print("speeding up")
                    self.ball.accelerate()
            self.collision_handler()
            self.draw()

    def collision_handler(self):
        if self.ball.rect.colliderect(self.player1.rect):
            self.ball.x_change = -self.ball.x_change
        elif self.ball.rect.colliderect(self.player2.rect):
            self.ball.x_change = -self.ball.x_change

        if self.ball.x + self.ball.width >= self.screen.get_width():
            pygame.quit()
            sys.exit()
        elif self.ball.x <= 0:
            pygame.quit()
            sys.exit()

        if self.ball.y + self.ball.height >= self.screen.get_height():
            self.ball.y_change = -abs(self.ball.y_change)
        elif self.ball.y <= 0:
            self.ball.y_change = abs(self.ball.y_change)

#        if self.player1.y + self.player1.height > self.screen.get_height():
#            self.player1.y = self.screen.get_height() - self.player1.height
#        elif self.player1.y < 0:
#            self.player1.y = 0

    def draw(self):
        self.screen.fill(Pong.COLOURS["WHITE"])         # not important
        self.ball.update()
        self.ball.render(self.screen)
        self.player1.update()
        self.player1.render(self.screen)
        self.player2.update()
        self.player2.render(self.screen)
        pygame.display.update()

if __name__ == "__main__":
    Pong().play()
