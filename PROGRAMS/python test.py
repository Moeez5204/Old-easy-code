fo = open("Python Test.txt", "a+")

again == "y"

while again :
    name=input("please type in a name: ")
    fo.write(name+"/n")
    again=input("Do you want to enter another name (Y/N)? ")
    again=again.upper()

fo.close
