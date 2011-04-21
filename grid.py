# -*- coding: utf-8 -*-
#
import pyglet
import pyglet.gl as gl
from obj3d import Obj3D

class Grid(Obj3D):
    # @param pos (x,y,z)
    # @param size (size_x,size_y)
    # @param nelem (nelem_x,nelem_y)
    def __init__(self,pos,size,n_elem):
        Obj3D.__init__(self)
    
        # por si se usa una tupla en el paramtro 'pos'
        self.pos[0]=pos[0]
        self.pos[1]=pos[1]
        self.pos[2]=pos[2]
        
        self.size=size
        self.n_elem=n_elem
        
        self.resetData()
        
        self.pos[0]+=10
        self.pos[1]+=20
        
    def resetData(self):
        self.data_x=[self.pos[0]+i*(float(self.size[0])/self.n_elem[0]) for i in xrange(0,self.n_elem[0]+1)]
        self.data_y=[self.pos[1]+i*(float(self.size[1])/self.n_elem[1]) for i in xrange(0,self.n_elem[1]+1)]
        self.data_z=[[self.pos[2] for i in xrange(0,self.n_elem[1]+1)] for j in xrange(0,self.n_elem[1]+1)]


    def draw(self):
        
        gl.glTranslatef(self.x,self.y,self.z)
    
       	gl.glColor3f(1.0, 0.0, 0.0)
    	
        for i in xrange(0,self.n_elem[0]):
        
            gl.glBegin(gl.GL_TRIANGLE_STRIP)

            gl.glVertex3f(self.data_x[i]  , self.data_y[0], self.data_z[i][0])
            gl.glVertex3f(self.data_x[i+1], self.data_y[0], self.data_z[i+1][0])

            for j in xrange(1,self.n_elem[1]):
                gl.glVertex3f(self.data_x[i],  self.data_y[j]  , self.data_z[i][j])
                gl.glVertex3f(self.data_x[i+1], self.data_y[j+1], self.data_z[i+1][j+1])
	
            gl.glVertex3f(self.data_x[i], self.data_y[self.n_elem[1]], self.data_z[i+1][self.n_elem[1]])

            gl.glEnd()

