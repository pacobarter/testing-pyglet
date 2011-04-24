# -*- coding: utf-8 -*-
#
import pyglet
from pyglet.gl import *

import mainwnd
import world

def initGL():
    glPolygonMode(GL_FRONT, GL_FILL)
    glPolygonMode(GL_BACK, GL_LINE)
    
    glEnable(GL_CULL_FACE)
    glFrontFace(GL_CCW)
    
    
#------------------------------------------------------
#   MAIN
#
if __name__=='__main__':
    frame_rate=60
    
    initGL()
    
    the_world=world.World()
    
    wnd=mainwnd.MainWnd(the_world)
    
    pyglet.clock.schedule_interval(wnd.update,1/float(frame_rate))
    pyglet.app.run()

