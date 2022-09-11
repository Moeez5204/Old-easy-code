def linearsearch(array,target):
    found = False
    i = 0

    while found == False:
        if  array[i] == target:
          found = True
          print(i,'is the index where the target located')
        else:
            i += 1

sequence = [1,3,5,7,9,2,4,6,8,0]
linearsearch(sequence,9)
        
    
