# -*- coding: utf-8 -*-
#

import pyglet
from pyglet.gl import *

from obj3d import Obj3D

class Camera(Obj3D):

    def __init__(self):
        Obj3D.__init__(self)
        
        self.ortho=False

        self.fov=60        
        self.lookAt=[0,0,0]
        self.upY=[0,0,1]
        
        self.persp_zlimits=[1,500]
        
        self.ortho_limits=[[-300,300], [-300,300], [-300,300]]
                     
        self.zoom=1

    def activate(self,width,height):
        if width>height:
            aspect=float(width)/float(height)
        else:
            aspect=float(height)/float(width)
    
        if self.ortho:
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()

            glOrtho(self.ortho_limits[0][0], self.ortho_limits[0][1], 
                    self.ortho_limits[1][0], self.ortho_limits[1][1], 
                    self.ortho_limits[2][0], self.ortho_limits[2][1])

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

        else:        
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(self.fov*self.zoom, aspect, self.persp_zlimits[0], self.persp_zlimits[1])
            
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(self.x,self.y,self.z, 
                      self.lookAt[0],self.lookAt[1],self.lookAt[2], 
                      self.upY[0],self.upY[1],self.upY[2])



    