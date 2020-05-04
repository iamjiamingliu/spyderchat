from py_folder import advanced_functions, forums, log_in, Messages_class, other_functions, Posts_class, Search_engine, Setting, SpyderChat, word_list

import sys
from colorama import Fore
import time

def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.05)

def opening():
  print_slow ("Great! Lets get started.\n")
  other_functions.clear()
  hallway()


def hallway():
  print_slow ("You walk straight through a dark hall until you reach two paths.\n")
  print_slow ("What do you do? turn left or turn right\n")
  b = input("\n")
  if (b == "left"):
    print_slow ("You turn to see what looks like a baby fox\n")
    foxtrap()
  elif (b == "right"):
    print_slow ("You fall into enderman spawner\n")
    enderman()
  else:
    hallway()

def enderman():
  print_slow ("\n")
  
def foxtrap():
  print_slow ("Do you run or walk up to the baby fox?\n")
  c = input("\n")
  if (c == "run"):
    print_slow ("You turn to run into the hall but the door has already been closed\n")
    print_slow ("You turn around and walk up to the fox\n")
    print_slow ("The fox looks at you and slowly puts on a green hat, all while laughing evily\n")
    foxtrap2()
  elif (c == "walk up"):
    print_slow ("The fox looks at you and slowly puts on a green hat, all while laughing evily\n")
    print_slow ("You now realize that you have made a grave mistake and walked into Teemo's den!!!\n")
    foxtrap2()
  else:
    foxtrap()
  
def foxtrap2():
  print_slow ("Do you attack or hide?\n")
  d = input("\n")
  if (d == "attack"):
    print_slow("You draw your broadsword that you bought for 350g\n")
    teemoattack()
  elif (d == "hide"):
    print_slow ("You run in a zigzag motion running into each of Teemo's hidden mushrooms\n")
    print_slow ("You are poisoned and, now, are a dead man('s plate ;) )\n")
    print_slow (Fore.RED + "GAME OVER\n")
    print_slow (Fore.WHITE + "\n")
  else:
    foxtrap2()
    
def teemoattack():
  print_slow ("Teemo pulls out his blowdart and readies for battle\n")
  print_slow ("What are you going to do? Straight Attack / Heal / Defend\n")
  e = input("\n")
  if(e == "attack"):
    attack()
  elif(e == "heal"):
    print_slow("You tried to heal, but you used the wrong potion. You are dead now!\n")
    time.sleep(2)
    
  elif(e == "defend"):
    print_slow("You tried to defend, but your enemy is much stroner than you!")
    print_slow("Defense failed, you are a dead man now!\n")
    time.sleep(2)
  else:
    teemoattack()

def attack():
  print_slow("swing, spin, throw\n")

def play_tic_tac_toe():
  import time
  print_slow ("Hey, Welcome in a TIC TAC TOE game!\n")
  time.sleep(2)
  print_slow ("Player 1 key is X\n")
  print_slow ("Player 2 key is O\n")
  print_slow ("Enjoy the game!\n")
  time.sleep(2)

  board = [0,1,2,3,4,5,6,7,8]

  def board_tally():
      print_slow ("-------------\n")
      print_slow ("| " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]) + " | \n")
      print_slow ("-------------\n")
      print_slow ("| " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]) + " | \n")
      print_slow ("-------------\n")
      print_slow ("| " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + " | \n")
      print_slow ("-------------\n")
      time.sleep(1.5)

  #board_tally()

  def player_choice():
      sum_X_0 = 0
      while True:
          
          count_O = board.count("X\n")
          count_X = board.count("O\n")
          sum_X_0 = count_O + count_X
          if sum_X_0 == 9:
              print_slow ("No Winner\n")
              return False
              
          player_1=input("Player 1 please select your slot:\n")
          while str(player_1) not in [str(x) for x in range(9)]:
            player_1=input("Sorry, please enter an valid option:\n")
          if board[int(player_1)] == "O":
              print_slow ("Hey Player 1!, Thats slot had been already taken.\n")
          elif board[int(player_1)] == "X":
              print_slow ("Hey Player 1!, Thats slot had been already taken.\n")
          else:
              board[int(player_1)] = "X"                        
          board_tally()

          if board[0:3] == ["X", "X", "X"]:
              print_slow ("Player 1 Wins\n")
              break
          if board[3:6] == ["X", "X", "X"]:
              print_slow ("Player 1 Wins\n")
              break
          if board[6:9] == ["X", "X", "X"]:
              print_slow ("Player 1 Wins\n")
              break
          if board[0:9:4] == ["X", "X", "X"]:
              print_slow ("Player 1 Wins\n")
              break
          if board[2:7:2] == ["X", "X", "X"]:
              print_slow ("Player 1 Wins\n")
              break
          if board[0:7:3] == ["X", "X", "X"]:
              print_slow ("Player 1 Wins\n")
              break
          if board[1:8:3] == ["X", "X", "X"]:
              print_slow ("Player 1 Wins\n")
              break
          if board[2:9:3] == ["X", "X", "X"]:
              print_slow ("Player 1 Wins\n")
              break
          
          count_O = board.count("X\n")
          count_X = board.count("O\n")
          sum_X_0 = count_O + count_X
          if sum_X_0 == 9:
              print_slow ("No Winner\n")
              return False

          player_2=input("Player 2 please select your slot:\n")
          while str(player_2) not in [str(x) for x in range(9)]:
            player_1=input("Sorry, please enter an valid option:\n")
          if board[int(player_2)] == "O":
              print_slow ("Hey Player 2!, Thats slot had been already taken.\n")
          elif board[int(player_2)] == "X":
              print_slow ("Hey Player 2!, Thats slot had been already taken.\n")
          else:
              board[int(player_2)] = "O"        
          board_tally()

          if board[0:3] == ["O", "O", "O"]:
              print_slow ("Player 2 Wins\n")
              break
          if board[3:6] == ["O", "O", "O"]:
              print_slow ("Player 2 Wins\n")
              break
          if board[6:9] == ["O", "O", "O"]:
              print_slow ("Player 2 Wins\n")
              break
          if board[1:9:4] == ["O", "O", "O"]:
              print_slow ("Player 2 Wins\n")
              break
          if board[2:7:2] == ["O", "O", "O"]:
              print_slow ("Player 2 Wins\n")
              break
          if board[0:7:3] == ["O", "O", "O"]:
              print_slow ("Player 2 Wins\n")
              break
          if board[1:8:3] == ["O", "O", "O"]:
              print_slow ("Player 2 Wins\n")
              break
          if board[2:9:3] == ["O", "O", "O"]:
              print_slow ("Player 2 Wins\n")
              break
          
  #player_choice()

  def continue_game():
      #player_choice()
      #user = "yes"
      #player1_score = 0
      while True:
          board[0:9] = [0,1,2,3,4,5,6,7,8]
          board_tally()
          player_choice()
          print_slow ("Do you want to play more? yes/no:\n")
          user = input("\n")
          if user == "yes":
              True
          elif user == "no":
              break

  continue_game()


