import pygame
import sys
from const import *
from animationPack import *


class GameWindow:
    def __init__(self, screen, timer, load_method):
        self.load_method = load_method
        self.screen = screen
        self.objects = self.load_method.objects
        self.timer = timer
        self.agen = AnimationInterface.AnimationMethodInterface(self.screen, self.timer,
                                                                FRAME_COUNTS,
                                                                self.objects,
                                                                self.load_method.get_load_objects())

    def game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if self.objects['Hector'].coordination[1] == self.objects['Hector'].earth:
                        self.objects['Hector'].status = 'RUN_R'
                        self.objects['Hector'].m_status = 'frame_run'
                if event.key == pygame.K_a:
                    if self.objects['Hector'].coordination[1] == self.objects['Hector'].earth:
                        self.objects['Hector'].status = 'RUN_L'
                        self.objects['Hector'].m_status = 'frame_run'
                if event.key == pygame.K_w:
                    self.objects['Hector'].m_status = 'frame_jump'
                    if self.objects['Hector'].status[-1] == 'R':
                        self.objects['Hector'].status = 'JUMP_R'
                    elif self.objects['Hector'].status[-1] == 'L':
                        self.objects['Hector'].status = 'JUMP_L'
                if event.key == pygame.K_h:
                    self.objects['Hector'].m_status = 'frame_hit'
                    if (self.objects['Hector'].status == 'STAY_R' or
                            self.objects['Hector'].status == 'RUN_R'):
                        self.objects['Hector'].status = 'HIT_R'
                    elif (self.objects['Hector'].status == 'STAY_L' or
                            self.objects['Hector'].status == 'RUN_L'):
                        self.objects['Hector'].status = 'HIT_L'
                    elif self.objects['Hector'].status == 'JUMP_R':
                        self.objects['Hector'].status = 'HIT_JUMP_R'
                    elif self.objects['Hector'].status == 'JUMP_L':
                        self.objects['Hector'].status = 'HIT_JUMP_L'
                if event.key == pygame.K_j:
                    self.objects['Hector'].m_status = 'frame_kick'
                    if (self.objects['Hector'].status == 'STAY_R' or
                            self.objects['Hector'].status == 'RUN_R'):
                        self.objects['Hector'].status = 'KICK_R'
                    elif (self.objects['Hector'].status == 'STAY_L' or
                            self.objects['Hector'].status == 'RUN_L'):
                        self.objects['Hector'].status = 'KICK_L'
                    elif self.objects['Hector'].status == 'JUMP_R':
                        self.objects['Hector'].status = 'KICK_JUMP_R'
                    elif self.objects['Hector'].status == 'JUMP_L':
                        self.objects['Hector'].status = 'KICK_JUMP_L'
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    if self.objects['Hector'].coordination[1] == self.objects['Hector'].earth:
                        self.objects['Hector'].status = 'STAY_R'
                        self.objects['Hector'].m_status = 'stay'
                if event.key == pygame.K_a:
                    if self.objects['Hector'].coordination[1] == self.objects['Hector'].earth:
                        self.objects['Hector'].status = 'STAY_L'
                        self.objects['Hector'].m_status = 'stay'
