import pygame
import LoadPack.interface
from EventManager import GameWindow
from MechManager import MechanicManager
from const import *


def run():
    pygame.init()
    screen = pygame.display.set_mode(STANDARD_SCREEN_SIZE)
    pygame.display.set_caption(NAME)
    timer = pygame.time.Clock()
    Lgen = LoadPack.interface.LoadMethodInterface(screen)
    Egen = GameWindow(screen, timer, Lgen)
    Mgen = MechanicManager(screen, Lgen)


    while True:
        timer.tick(12)
        screen.fill(STANDARD_BG_COLOR)
        Egen.game_events()
        Mgen.claim_info()
        Mgen.calculation(cal=True)
        Egen.agen.output()
        Lgen.get_runtime_load()
        pygame.display.flip()


if __name__ == '__main__':
    run()

