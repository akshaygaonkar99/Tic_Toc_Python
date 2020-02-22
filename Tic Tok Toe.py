Board = ['T','.','.',
          '.','.','.',
          '.','.','.','.']

def Display_board():
  Play_board1 = Board[1] + '|' + Board[2]+'|'+Board[3]
  Play_board2 = Board[4] + '|' + Board[5]+'|'+Board[6]
  Play_board3 = Board[7] + '|' + Board[8]+'|'+Board[9]
  print(Play_board1)
  print(Play_board2)
  print(Play_board3)
player = "X"
game_running = True
winner_status = False

def flip_player():
  global player
  if player == "X":
    player= "O"
  elif player == "O":
    player = "X"
  return

def game_end():
  global game_running
  game_running = False
  for i in Board:
    if i==".":
      
      game_running = True
  if winner_status == True:
    game_running = False
  return

def check_for_win():
  rows()
  column()
  adjecent()

def rows():
  global winner_status
  if Board[1] == Board[2]==Board[3] != ".":
    print("Winner is "+ player)
    winner_status = True
  if Board[4] == Board[5]==Board[6] != ".":
    print("Winner is "+ player)
    winner_status = True
  if Board[7] == Board[8]==Board[9] != ".":
    print("Winner is "+ player)
    winner_status = True

def column():
  global winner_status
  if Board[1] == Board[4]==Board[7] != ".":
    print("Winner is "+ player)
    winner_status = True
  if Board[2] == Board[5]==Board[8] != ".":
    print("Winner is "+ player)
    winner_status = True
  if Board[9] == Board[6]==Board[9] != ".":
    print("Winner is "+ player)
    winner_status = True

def adjecent():
  global winner_status
  if Board[1] == Board[5]==Board[9] != ".":
    print("Winner is "+ player)
    winner_status = True
  if Board[3] == Board[5]==Board[7] != ".":
    print("Winner is "+ player)
    winner_status = True



def Play_game():
  while game_running:
    print(" ")

    print("Control to -> "+player)
    valid = False
    while not valid:
      position = input("Enter the position:")
      position= int(position)
      while position not in [3,1,2,4,5,6,7,8,9]:
        print("While enterd")
        position=input("invalid entry, select 1-9: ")
        position= int(position)
        print("position value is:"+str(position))


      if Board[position] == ".":
        valid = True
      else:
        print("You can't overwrite in that position.")
      
    print(" ")
    Board[position]= player
    Display_board()
    
    check_for_win()
    flip_player()
    game_end()
  print("Game End")
  print("8 8")
  print(" Akshay ")


print("Tic Tok Toe")
Display_board()
Play_game()
