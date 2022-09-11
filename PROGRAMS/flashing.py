import time

Z = 0 
Y = int(input("please type in amount of times you want to repeat the message"))
X = input("please input a messagae below 20 charcters")
if len(X) > 20 :
    print ("error")
else:
    
    while Z <= Y :
        
         print (X)
         time.sleep(1)
         Z = Z + 1

    
