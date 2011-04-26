# -*- coding: utf-8 -*-
#
import math
import pyglet
from pyglet.gl import *
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

        # init GL options
        glEnable(GL_CULL_FACE)
        glFrontFace(GL_CCW)
        glCullFace(GL_BACK)

        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_LINE)

        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        
        # create the world
        self.the_world=a_world
        
        # create the camera
        self.the_camera=camera.Camera()
        
        self.the_camera.x=400
        self.the_camera.y=-350
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
        
        angle_xy=2*math.pi*x/float(self.width)
#        self.the_camera.orbitXY(angle_xy)

        angle_z=math.pi*(y/float(self.height)-0.5)
#        self.the_camera.orbitZ(angle_z)

        self.the_camera.orbit(angle_xy,angle_z)

    #   Keyboard events
    #
    def on_key_press(self,symbol,modif):
        self.the_world.on_key_press(symbol,modif)
        
