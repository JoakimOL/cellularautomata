import time
import random
import pygame
import logging

from pygame.locals import *
from automata import Simple_Automata
from rps_automata import RPS_Automata
from gol_automata import GOL_Automata
from powder_automata import Powder_Automata

class App:
    def __init__(self, type, use_fonts = False, wrap = True):
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
        if(type == "rps"):
            self.automata = RPS_Automata(self.width//8,self.height//8,self.size,wrap=wrap, spiral=False, font=self.system_font)
            # self.automata = RPS_Automata(10,10,self.size,wrap=wrap, spiral=False, font=self.system_font)
        elif(type == "rps_spiral"):
            self.automata = RPS_Automata(self.width//8,self.height//8,self.size,wrap=wrap, spiral=True, font=self.system_font)
            # self.automata = RPS_Automata(10,10,self.size,wrap=wrap, spiral=True, font=self.system_font)
        elif(type == "gol"):
            self.automata = GOL_Automata(self.width//8,self.height//8, self.size, wrap, self.system_font)
            # self.automata = GOL_Automata(10,10, self.size, wrap, self.system_font)
        elif(type == "powder"):
            self.automata = Powder_Automata(self.width//8,self.height//8, self.size, wrap=wrap, font=self.system_font)
            # self.automata = Powder_Automata(10,10, self.size, wrap=wrap, font=self.system_font)
        else:
            self.automata = Simple_Automata(self.width//8,self.height//8, self.size, wrap, self.system_font)
            # self.automata = Simple_Automata(10,10, self.size, wrap, self.system_font)
        self.dt = 0 # time since last frame
        self.updates = 0 # number of frame last second
        self.last_second = 0 # timestamp of when we started counting updates
        self.last_frame = 0 # timestamp of last frame we drew
        self._FRAME_TIME_GOAL = 1/20 # Aiming for 20 fps
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
            self.handle_mouse_move_event(event.pos, None)
            self.drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if(self.drawing):
                self.handle_mouse_move_event(event.pos, event.rel)
            
    def handle_key_event(self, key, unicode):
        # Global key bindings
        if key == pygame.K_ESCAPE or key == pygame.K_q:
            self.should_exit = True
        elif key == pygame.K_SPACE:
            self.logger.info("space!")
            self.running = not self.running
            self.run()
        elif key == pygame.K_s:
            if(not self.running):
                self.loop()
                self.render()
        else:
            # automata specific keybindings
            self.automata.handle_key_event(key, unicode)
        
    def handle_mouse_press_event(self, pos, button):
        x, y = pos
        translated_pos = x // self.automata.CELLSIZE, y // self.automata.CELLSIZE
        self.automata.mouse_click_at(translated_pos)
        pygame.display.update()

    def handle_mouse_move_event(self, pos, rel):
        x, y = pos
        if(x > self.width-1 or y > self.height-1):
            return
        translated_pos = x // self.automata.CELLSIZE, y // self.automata.CELLSIZE
        self.automata.mouse_click_at(translated_pos)
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
            if(self.dt > self._FRAME_TIME_GOAL):
                if(self.running):
                    self.loop()
                    self.updates += 1
                self.render()
                self.last_frame = current_time
                self.dt = 0
            else:
                time_to_sleep = self._FRAME_TIME_GOAL - self.dt
                time.sleep(time_to_sleep)
