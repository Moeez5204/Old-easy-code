def hanoi(n, tower1, tower2, tower3):
    if n > 0:
        hanoi(n - 1, tower1, tower2, tower3)
        if tower1:
            tower2.append(tower1.pop())
  
        hanoi(n - 1, tower3, tower1, tower2)
        
tower1 = [4,3,2,1]
tower2 = []
tower3 = []
hanoi(len(tower1),tower1,tower3,tower2)

print(tower1, tower2, tower3)
