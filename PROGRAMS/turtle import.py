from turtle import *

from random import randint # from the random module import the function randint
#like turtle it is a module, read ahead for use

speed(0)

bgcolor('black')

x = 1

while x < 400:



    colormode(255) # this is something that is irrelevant at this point
               # check the pythondocs link at the end for more info


    pencolor(4,6,10) # changes the color of the pen to the rgb coordinates
                    # obtained by the variables r, g, b changing each time

    fd(50 + x)
    rt(90.911)


    x = x+1 

exitonclick() 

#again, try to customize  






