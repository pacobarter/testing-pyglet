#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import pyglet
import mainwnd
import world

#------------------------------------------------------
#   MAIN
#
if __name__=='__main__':
    frame_rate=60

    the_world=world.World()
    
    wnd=mainwnd.MainWnd(the_world)
    
    pyglet.clock.schedule_interval(wnd.update,1/float(frame_rate))
    pyglet.app.run()

