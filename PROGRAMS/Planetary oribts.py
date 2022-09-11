import math

global t
global x
global y
t = 0

def pos(x,y,DFS,t):
    x = DFS * math.cos(t)
    y = DFS * math.sin(t)
    t += 1

    print(x,y,t)
   
while t < 100:
    t += 0.01

    pos(7,6,1,t)
