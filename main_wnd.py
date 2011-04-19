import pyglet
import pyglet.gl as gl
from pyglet.window import key
from pyglet.window import mouse

#------------------------------------------------------
#   window class 
#
class MyWnd(pyglet.window.Window):
    def __init__(self):
        super(MyWnd,self).__init__()
        
        self.label=pyglet.text.Label('Hi world!')
        self.label.x=10
        self.label.y=10

    def update(self,dt):
        pass
        

    #   Draw event
    #
    def on_draw(self):
        self.clear()
        self.label.draw()

        gl.glLoadIdentity()

	gl.glColor3i(100,0,0,200)
	gl.glBegin(gl.GL_TRIANGLES)
   	gl.glColor3f(1.0, 0.0, 0.0)
    	gl.glVertex3f(0.0, 0.0, 0.0)
    	gl.glVertex3f(150.0, 0.0, 0.0)
    	gl.glVertex3f(150.0, 150.0, 0.0)
	gl.glEnd()

    #   Mouse events
    #
    def on_mouse_press(self,x,y,buttons,modifiers):
        pass

    def on_mouse_release(self,x,y,buttons,modifiers):
        pass

    def on_mouse_drag(self,x,y,dx,dy,buttons,modifiers):
        self.label.x=x
        self.label.y=y

    #   Keyboard events
    #
    def on_key_press(self,symbol,modif):
        pass

#------------------------------------------------------
#   MAIN
#
if __name__=='__main__':
    frame_rate=60
    
    wnd=MyWnd()
    
    pyglet.clock.schedule_interval(wnd.update,1/float(frame_rate))
    pyglet.app.run()