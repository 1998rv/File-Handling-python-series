# Developer Name :- Ravi Kumawat
# Date :- 13-12-2023
# Code :- always online in your team

from time import sleep #========= import library
import math #========= import library
from clicknium import clicknium as cc #========= import library

def circle():
    a,b = cc.mouse.position()
    w = 20
    m = (2*math.pi)/w
    r = 200
# ======================================
    while 1:
        for i in range(0, w+1):
            x = int(a+r*math.sin(m*i))
            y = int(b+r*math.cos(m*i))
            cc.mouse.move(x,y)
            sleep(1)
# =======================================
if __name__ == "__main__":
    circle()
