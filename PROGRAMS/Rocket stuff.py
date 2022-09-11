import math

def GravityForce(mass1,mass2,distance):
    global force
    G = 6.67*10**-11
    temp = mass1 * mass2 * G
    force = temp/distance**2

def timeneeded(U,A,S):
    Time = ''
    TempaA = math.sqrt((U**2)-4*A*S)
    TEMPT1 = (-U + TempaA)
    T1 = TEMPT1 / 2*A
    TEMPT2 = (-U - TempaA)
    T2 = TEMPT2 / 2*A

    if T1 > 0 and T2 <= 0:
       Time = T1
    elif T2  > 0 and T1 <= 0:
       Time = T2
    elif T2 > 0 and T1 > 0:
        if T2 > T1:
            Time = T2
        else:
            Time = T1
    print(Time)

   

        
GravityForce(7,23,45)
timeneeded(78,8,8)


def attraction(mass1,mass2,force):
    if mass1 > mass2 :
        attractor = mass1
    else:
        attractor = mass2

    accelration = force/attractor
    

