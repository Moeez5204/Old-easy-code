def GravityForce(mass1, mass2, distance):
    global force
    G = 6.67 * 10 ** -11                  #gravity calculator
    temp = mass1 * mass2 * G
    force = temp / (6400000 + distance) ** 2
    return force



for i in range(10):
    print(GravityForce(200000000,300000000,i))

