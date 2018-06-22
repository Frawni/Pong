import pygame
import sys


class Pong(object):
    def __init__(self):
        pygame.init()
        for _ in range(pygame.joystick.get_count()):
            pygame.joystick.Joystick(_).init()

    def play(self):
        clock = pygame.time.Clock()
        pygame.time.set_timer(1, 5000)
        while True:
            clock.tick(50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.JOYAXISMOTION:
                    print("JOYAXISMOTION", event.axis, event.value)
                if event.type == pygame.JOYBALLMOTION:
                    print("JOYBALLMOTION", event.ball, event.rel)
                if event.type == pygame.JOYHATMOTION:
                    print("JOYHATMOTION", event.hat, event.value)
                if event.type == pygame.JOYBUTTONUP:
                    print("JOYBUTTONUP", event.button)
                if event.type == pygame.JOYBUTTONDOWN:
                    print("JOYBUTTONDOWN", event.button)
                if event.type == pygame.USEREVENT:
                    print("USERVENT", event.code)


if __name__ == "__main__":
    Pong().play()
