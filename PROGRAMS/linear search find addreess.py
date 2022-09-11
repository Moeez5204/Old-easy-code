def linearsearch(array,target):
    found = False
    i = 0

    while found == False:
        if  array[i] == target:
          found = True
          return(i)
        else:
            i += 1

names = ['hamza','moeez','saugat','mattan']
address= ['69 weed palace','buckhighman palace','Everest','unknown']
phonenumber = ['074047189863','07422664985','07380360995','07732857118']

finder = linearsearch(names,'saugat')


print('the address is',address[finder],
                               'and his phone number is ',phonenumber[finder])
