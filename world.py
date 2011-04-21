# -*- coding: utf-8 -*-
#
import pyglet
import pyglet.gl as gl
from pyglet.window import key
from pyglet.window import mouse

import grid

class World:

    #   Init
    #
    def __init__(self):
        self.objects=[]

        label=pyglet.text.Label('Hi world!')
        label.x=100
        label.y=100
        self.add(label)
        
        gr=grid.Grid((0,0,0),(300,300),(10,20))
        self.add(gr)
        
        self.idx=0
    
    def add(self,obj):
        self.objects.append(obj)


    #   Update event
    #
    def update(self,dt):
        pass
        

    #   Draw event
    #
    def draw(self):
        for obj in self.objects:
            obj.draw()


    #   Mouse events
    #
    def on_mouse_press(self,x,y,buttons,modifiers):
        pass

    def on_mouse_release(self,x,y,buttons,modifiers):
        pass

    def on_mouse_drag(self,x,y,dx,dy,buttons,modifiers):
        o=self.objects[self.idx]
        o.x=x
        o.y=y

    #   Keyboard events
    #
    def on_key_press(self,symbol,modif):
        if symbol==key.SPACE:
            self.idx=(self.idx+1) % 2
        
