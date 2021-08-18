import sys
import random
from gl import Render

def Mickey():
    r = Render(1200, 1200)
    r.load('./Mickey.obj', (12, 6, 8), (50, 50, 50))
    r.display('resultado.bmp')

Mickey()