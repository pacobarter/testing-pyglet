# -*- coding: utf-8 -*-
#

import threading
import pyglet
import mainwnd

class GLWndThrd(threading.Thread):

    def __init__(self,world,frame_rate):
        super(GLWndThrd,self).__init__()

        self.frame_rate=frame_rate

        self.the_world=world
        self.wnd=mainwnd.MainWnd(self.the_world)

        pyglet.clock.schedule_interval(self.wnd.update,1/float(self.frame_rate))

    def run(self):
        pyglet.app.run()

