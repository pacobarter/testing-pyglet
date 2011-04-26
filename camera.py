# -*- coding: utf-8 -*-
#

import math
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
        
        self.persp_zlimits=[1,1500]
        
        self.ortho_limits=[[-300,300], [-300,300], [-300,300]]
                     
        self.zoom=1

    # angle in radians
    def orbitXY(self, angle):
        nx=self.x-self.lookAt[0]
        ny=self.y-self.lookAt[1]
        
        ro=math.sqrt(nx**2+ny**2)

        self.x=self.lookAt[0]+ro*math.cos(angle)
        self.y=self.lookAt[1]+ro*math.sin(angle)

    def orbitZ(self,angle):
        nx=self.x-self.lookAt[0]
        ny=self.y-self.lookAt[1]
        nz=self.z-self.lookAt[2]
        
        ro3=math.sqrt(nx**2+ny**2+nz**2)
        angleXY=math.atan2(ny,nx)
        
        self.x=self.lookAt[0]+ro3*math.cos(angleXY)*math.cos(angle)
        self.y=self.lookAt[1]+ro3*math.sin(angleXY)*math.cos(angle)
        self.z=self.lookAt[1]+ro3*math.sin(angle)

    def orbit(self,angle_xy,angle_z):
        nx=self.x-self.lookAt[0]
        ny=self.y-self.lookAt[1]
        nz=self.z-self.lookAt[2]
        
        ro3=math.sqrt(nx**2+ny**2+nz**2)
        
        self.x=self.lookAt[0]+ro3*math.cos(angle_xy)*math.cos(angle_z)
        self.y=self.lookAt[1]+ro3*math.sin(angle_xy)*math.cos(angle_z)
        self.z=self.lookAt[1]+ro3*math.sin(angle_z)


    def activate(self,width,height):
        if width>height:
            aspect=float(width)/float(height)
        else:
            aspect=float(height)/float(width)
    
        if self.ortho:
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()

            if width>height:
                glOrtho(self.ortho_limits[0][0]*aspect, self.ortho_limits[0][1]*aspect, 
                        self.ortho_limits[1][0], self.ortho_limits[1][1], 
                        self.ortho_limits[2][0], self.ortho_limits[2][1])
            else:
                glOrtho(self.ortho_limits[0][0], self.ortho_limits[0][1], 
                        self.ortho_limits[1][0]*aspect, self.ortho_limits[1][1]*aspect, 
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



    