from OpenGL.GL import *
from OpenGL.GLUT import *

PALETTE = {
    'crashblue': (0.035, 0.031, 0.549)
}

def getColor(k):
    return PALETTE.get(k, (1, 1, 1))

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glutSwapBuffers()

def animate():
    glutPostRedisplay()

def keybinds(key, x, y):
    if key == b"w":
        pass
    if key == b"s":
        pass
    if key == b"a":
        pass
    if key == b"d":
        pass

def main():
    global win_w, win_h
    win_w, win_h = 300, 200
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(win_w, win_h)
    glutCreateWindow(b"Progressbar")
    glutDisplayFunc(display)
    glutIdleFunc(animate)
    glutKeyboardFunc(keybinds)
    glMatrixMode(GL_PROJECTION)
    glOrtho(0, win_w, win_h, 0, -1, 1)
    glClearColor(*getColor("crashblue"), 1)
    glutMainLoop()

if __name__ == '__main__': main()