import math

def Eorbits(a,b):
        x =  math.cos(t) * a # t is the time refrence which increases incremently
        y =  math.sin(t) * b # a and b are the center of the object they are orbiting
        print(x,y)


global t
t = 0

while t < 1:
    t += 0.01
    Eorbits(10,5)
    print(t)

    
