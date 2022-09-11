string = "CCMCCCCLLCCC"
Extra = "YYYYDHFKDUUUUUUUDHFHFHUUUUUFDFHFHFUUUERUIURIUKNNJFDSJHHJHJHJHHJJJJJJJJJJJJJJJDFFGFGYFGYGFYYFGYFG"


def SearchLongest(string):
    Array  = list(string)
    LongestLetter = ""
    LongestLenght = 0
    CurrentLenght = 0
   
    for i in range(0,len(Array)-1):
      if Array[i] == Array[i+1]: 
        CurrentLenght += 1
      else:
        CurrentLenght = 1
        CurrentLetter = Array[i]

      if CurrentLenght > LongestLenght:
        LongestLenght = CurrentLenght
        LongestLetter = Array[i]

    print(LongestLetter,"is the longest letter, with ",LongestLenght,"repeats in a single time")
        
SearchLongest(Extra)
