import time
import random
import pygame
import logging

from pygame.locals import *
from automata import Automata
from cell import Cell

class App:
    class ColorPicker:
        def __init__(self):
            self.selected_color = (0,0,0)
            self.RED = (255,0,0)
            self.GREEN = (0,255,0)
            self.BLUE = (0,0,255)
            self.BLACK = (0,0,0)

            self.colors = {
                "red": self.RED,
                "green": self.GREEN,
                "blue": self.BLUE,
                "black": self.BLACK
            }

    def __init__(self, use_fonts = False):
        self.colorpicker = self.ColorPicker()
        self.running = False
        self.should_exit = False
        pygame.init()
        if(use_fonts):
            pygame.font.init()
            self.system_font = pygame.font.SysFont(None,18)
        else:
            self.system_font = None

        self.surface = None
        self.size = self.width, self.height = 800, 800
        self.automata = Automata(200,200, self.size, self.colorpicker.colors, self.system_font)
        self.dt = 0 # time since last frame
        self.updates = 0 # number of frame last second
        self.last_second = 0 # timestamp of when we started counting updates
        self.last_frame = 0 # timestamp of last frame we drew
        self._FRAME_TIME_GOAL = 1/10 # Aiming for 10 fps
        self.drawing = False
        self.logger = logging.getLogger()
        self.surface = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.update()
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type  == pygame.KEYUP:
            self.handle_key_event(event.key, event.unicode)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.drawing = False
        elif event.type == pygame.MOUSEMOTION:
            # self.handle_mouse_press_event(event.pos, event.button)
            if(self.drawing):
                self.handle_mouse_move_event(event.pos, event.rel)
            
    def handle_key_event(self, key, unicode):
        if key == pygame.K_ESCAPE or key == pygame.K_q:
            self.should_exit = True
        elif key == pygame.K_SPACE:
            self.logger.info("space!")
            self.running = not self.running
            self.run()
        elif key == pygame.K_1:
            self.logger.info("selected red")
            self.colorpicker.selected_color = self.colorpicker.colors["red"]
        elif key == pygame.K_2:
            self.logger.info("selected green")
            self.colorpicker.selected_color = self.colorpicker.colors["green"]
        elif key == pygame.K_3:
            self.logger.info("selected blue")
            self.colorpicker.selected_color = self.colorpicker.colors["blue"]
        elif key == pygame.K_4:
            self.logger.info("selected black")
            self.colorpicker.selected_color = self.colorpicker.colors["black"]
        else:
            self.logger.info(f"unhandled input: {unicode}")
        
    def handle_mouse_press_event(self, pos, button):
        x, y = pos
        translated_pos = x // self.automata.CELLSIZE, y // self.automata.CELLSIZE
        self.automata.mouse_click_at(translated_pos, button, self.colorpicker.selected_color)
        pygame.display.update()
        # self.logger.info(f"mousepos: {pos} button: {button}")

    def handle_mouse_move_event(self, pos, rel):
        print(pos,rel)
        x, y = pos
        if(x > self.width-1 or y > self.height-1):
            return
        translated_pos = x // self.automata.CELLSIZE, y // self.automata.CELLSIZE
        self.automata.mouse_click_at(translated_pos, self.colorpicker.selected_color)
        pygame.display.update()

            
    def loop(self):
        self.automata.apply_rule()
        self.automata.commit_rule_result()

    def render(self):
        self.automata.draw(self.surface)
        pygame.display.update()

    def exit(self):
        pygame.quit()
 
    def run(self):
        while(not self.should_exit):
            for event in pygame.event.get():
                self.on_event(event)
            current_time = time.time()
            if current_time - self.last_second> 1:
                self.logger.info(f"drew {self.updates} last second")
                self.updates = 0
                self.second = 0
                self.last_second = current_time
            self.dt = current_time - self.last_frame
            if(self.running):
                if(self.dt > self._FRAME_TIME_GOAL):
                    self.loop()
                    self.render()
                    self.last_frame = current_time
                    self.updates += 1
                    self.dt = 0
                else:
                    time_to_sleep = self._FRAME_TIME_GOAL - self.dt
                    time.sleep(time_to_sleep)
            else:
                if(self.dt > self._FRAME_TIME_GOAL):
                    self.render()
                    self.last_frame = current_time
                    self.dt = 0
                else:
                    time_to_sleep = self._FRAME_TIME_GOAL - self.dt
                    time.sleep(time_to_sleep)
