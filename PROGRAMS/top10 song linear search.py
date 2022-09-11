top10 = ['song1','song2','song3','song4','song5','song6','song7','song8'
         ,'song9','song10']



def linearsearch(array,target):
    found = False
    i = 0

    while found == False:
        if  array[i] == target:
          found = True
          print(i,'is the index where the target located')
        else:
            i += 1

linearsearch(top10,'song4')
