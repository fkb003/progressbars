from OpenGL.GL import *
from OpenGL.GLUT import *
import sys

PALETTE = {
    'crashblue': (0.035, 0.031, 0.549),
    'white': (1, 1, 1)
}

def getColor(k):
    return PALETTE.get(k, (1, 1, 1))

def display():
    global bar
    glClear(GL_COLOR_BUFFER_BIT)
    bar.draw()
    glutSwapBuffers()

def animate():
    glutPostRedisplay()

def keybinds(key, x, y):
    global bar
    step = 1
    if key == b"w":
        pass
    if key == b"s":
        pass
    if key == b"a":
        bar.update(-step)
    if key == b"d":
        bar.update(step)

def getTitle():
    if len(sys.argv) == 2:
        title = sys.argv[1].encode("utf-8")
    else:
        title = b"Progressbar"
    return title

class Bar:
    def __init__(self, p=0):
        global win_w, win_h
        self.progress = p
        self.x = win_w/2
        self.y = win_h/2
    def update(self, v):
        self.progress += v
        self.clamp()
    def clamp(self):
        if self.progress > 100:
            self.progress = 100
        elif self.progress < 0:
            self.progress = 0

    def draw(self):
        height = 20
        width = 200
        filled = width * (self.progress/100)

        glBegin(GL_QUADS)
        glColor3f(*getColor('white'))
        glVertex2f(self.x - width/2, self.y - height/2)
        glVertex2f(self.x - width/2 + filled, self.y - height/2)
        glVertex2f(self.x - width/2 + filled, self.y + height/2)
        glVertex2f(self.x - width/2, self.y + height/2)
        glEnd()

        glBegin(GL_LINES)
        glColor3f(*getColor('white'))
        glVertex2f(self.x - width/2, self.y - height/2)
        glVertex2f(self.x + width/2, self.y - height/2)
        glVertex2f(self.x + width/2, self.y - height/2)
        glVertex2f(self.x + width/2, self.y + height/2)
        glVertex2f(self.x + width/2, self.y + height/2)
        glVertex2f(self.x - width/2, self.y + height/2)
        glVertex2f(self.x - width/2, self.y + height/2)
        glVertex2f(self.x - width/2, self.y - height/2)
        glEnd()

def main(title):
    global win_w, win_h, bar
    win_w, win_h = 300, 200
    bar = Bar()
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(win_w, win_h)
    glutCreateWindow(title)
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutKeyboardFunc(keybinds)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, win_w, win_h, 0, -1, 1)
    glClearColor(*getColor("crashblue"), 1)
    glutMainLoop()

title = getTitle()
if __name__ == '__main__': main(title)