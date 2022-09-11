import math

global t
global x
global z #allows function to access and change functions
         #which can always be used

t = 0 #every object reacts as time increases 

def pos(x,y,DFS,t):
    x = DFS * math.cos(t) #change x coordinate
    z = DFS * math.sin(t) #change z coordinate
    

    print(x,z,t)
    
while t < 100: #Subsitute for main function
    t += 0.1  #Increases time

    pos(7,6,6300,t)


