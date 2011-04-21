# -*- coding: utf-8 -*-
#

class Obj3D:
    ''' 
    Base class for objects with dynamics
    '''

    def __init__(self):
        self.pos=[0,0,0]        # en m
        self.vel=[0,0,0]        # en m/s
        self.accel=[0,0,0]      # en m/s**2
        self.m=1                # en Kg
        
    def get_x(self):
        return self.pos[0]

    def set_x(self,nx):
        self.pos[0]=nx

    def get_y(self):
        return self.pos[1]

    def set_y(self,ny):
        self.pos[1]=ny

    def get_z(self):
        return self.pos[2]

    def set_z(self,nz):
        self.pos[2]=nz

    x=property(get_x,set_x)
    y=property(get_y,set_y)
    z=property(get_z,set_z)

