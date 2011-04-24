# -*- coding: utf-8 -*-
#
import pyglet
import pyglet.gl as gl
from pyglet.window import Window
from pyglet.window import key
from pyglet.window import mouse

import camera

#------------------------------------------------------
#   window class 
#
class MainWnd(Window):
    #   Init
    #
    def __init__(self,a_world):
        # super(MainWnd,self).__init__()
        Window.__init__(self)

        self.the_world=a_world
        self.the_camera=camera.Camera()
        
        self.the_camera.x=300
        self.the_camera.y=-150
        self.the_camera.z=80
        
    #   Update event
    #
    def update(self,dt):
        self.the_world.update(dt)
        

    #   Draw event
    #
    def on_draw(self):
        self.clear()
        
        self.the_camera.activate(self.width, self.height)

        self.the_world.draw()

    #   Mouse events
    #
    def on_mouse_press(self,x,y,buttons,modifiers):
        self.the_world.on_mouse_press(x,y,buttons,modifiers)

    def on_mouse_release(self,x,y,buttons,modifiers):
        self.the_world.on_mouse_release(x,y,buttons,modifiers)

    def on_mouse_drag(self,x,y,dx,dy,buttons,modifiers):
        self.the_world.on_mouse_drag(x,y,dx,dy,buttons,modifiers)

    #   Keyboard events
    #
    def on_key_press(self,symbol,modif):
        self.the_world.on_key_press(symbol,modif)
        
