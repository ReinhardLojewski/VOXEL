# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 14:24:33 2022

@author: loje_re
"""

import pygame
import numba

import pygame as pg
from player import Player
from voxel_render import VoxelRender

class App:
    def __init__(self):
        self.res = self.width, self.height = (800, 450)
        self.screen = pg.display.set_mode(self.res, pg.SCALED)
        self.clock = pg.time.Clock()
        self.player = Player()
        self.voxel_render = VoxelRender(self)
        

    def update(self):
        self.player.update()
        self.voxel_render.update()

    def draw(self)    :
        self.voxel_render.draw()
        pg.display.flip()
    
    def run(self):
        while True:
            
            self.update()
            self.draw()
            
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick(60)
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')
            
            # program termination via esc key in player.py
    
    
if __name__=='__main__':
    app = App()
    app.run()