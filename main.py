



def game():
  score = 0
  flag = False
  while not flag:
    
    kill = input("what number you have 1,2")
    
    if kill=="1":
      score += 1
      print(score)
      
    else:
      
      
      game()

game()
