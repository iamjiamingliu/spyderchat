from py_folder import advanced_functions, forums, log_in, Messages_class, other_functions, Posts_class, Search_engine, Setting, SpyderChat, word_list

import pickle
from validate_email import validate_email
import os
from termcolor import colored

import time
import random

import sys
def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.05)

file_path = 'central_db_folder/AV.txt'
foreverAV = {}

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')


User_manual = '''
---------------------------------------------------------------
Here is how you can use SpyderChat:

1. You can access numerous functions such as sending/recieving messages to different users

2. SpyderChat provides communication to user by provide message sending function

3. SpyderChat also provides entertainment. You can play games in SpyderChat

4. SpyderChat will NEVER reveal all the information about the user

If you still have question, feel free to spydermail admin1 or admin2 at anytime. Enjoy the program!
                          ------------ Admin and Admin2 2020
'''

def log_in1():
  if os.stat(file_path).st_size != 0:
    SpyderChat.accounts_dictionary = pickle.load(open("central_db_folder/AV.txt","rb"))

  input_username1 = SpyderChat.remove1(str(input('''
  --------------------------------------------
  Enter your username: 
  ''')))

  while input_username1 not in            SpyderChat.accounts_dictionary.keys():
    input_username1 = SpyderChat.remove1(str(input('''
  --------------------------------------------
  Sorry, username does not exist!
  Enter your username again 
  or [C]reate new accounts  [E]xit:
  ''')))
    if input_username1 == 'c':
      SpyderChat.create_account(other_functions.f1_var)
      other_functions.first_option()

    elif input_username1 == 'e':
      SpyderChat.exit1()
      time.sleep(10)



  input_password1 = str(input('''
  --------------------------------------------
  Enter your password: 
  '''))

  while input_password1 != SpyderChat.accounts_dictionary[input_username1].password:
    print_slow("let's see...")
    time.sleep(3)
    input_password1 = str(input('''
    --------------------------------------------
    Sorry, wrong password!
    Try again, or 
    [R]etreive Account [E]xit [C]reate New Account: 
    '''))
    if input_password1 == 'c':
      SpyderChat.create_account(other_functions.f1_var)
      other_functions.first_option()
    elif input_password1 == 'e':
      SpyderChat.exit1()


    elif input_password1 == 'r':
      other_functions.retreive_account(input_username1)
      other_functions.first_option()

  print_slow("")
  print_slow("You have succesfully logged in!")
  time.sleep(0.5)
  clear()
  return input_username1
  


def logged_in(username):
  
  print_slow('''
  -----------------------------------------------------------
  Welcome, %s !       
    " %s "
                             --- %s
  ''' %(username, SpyderChat.accounts_dictionary[username].personal_comments, SpyderChat.accounts_dictionary[username].real_name))
  time.sleep(1.5)
  second_option()
  
def second_option():

  logged_in_option1 = str(input(colored(
  '''
  -----------------------------------------------------
  Would you like to visit:
  [M]ailbox              Time to check your Spydermail! 
  [P]osts & Friends      Why not network and post?
  [C]hatroom & Forums    You need Spyderlike-interaction
  [G]ames & Setting      Edit your profile & Epic Games
  [S]earch          [H]elp          [B]ack         
  ''', "green"))).lower()
  
  while logged_in_option1 not in ['m','p','h','c','s','b', 'g']:
    logged_in_option1 = str(input('''
    -----------------------------------------------------
    Sorry, only choose one of the following options!
    Would you like to visit:
    [M]ailbox              Time to check your Spydermail! 
    [P]osts & Friends      Why not network and post?
    [C]hatroom & Forums    You need Spyderlike-interaction
    [G]ames & Setting      Edit your profile & Epic Games
    [S]earch          [H]elp          [B]ack    
    '''))

  if logged_in_option1 == 'p':
    Posts_class.post_menu()
  if logged_in_option1 == 'h':
    print_slow(User_manual)
    time.sleep(6)
    print_slow("Hopefully that helped. Now,")
    stop_reading = str(input(("Hit Enter to go back: ")))
    while stop_reading not in ['',' ','   ','    ']:
      stop_reading = str(input(("Hit Enter to go back: ")))
    second_option()

  if logged_in_option1 == 'c':
    forums.entered_option()
    second_option()

  elif logged_in_option1 == 'b':
    print_slow('''
    --------------------------------------------
    ''')
    print_slow(str('               ' + random.choice(['Have a nice day!', 'Great! See you later!', 'Goodbye!', 'Bye-bye, Adios!', 'Bye-bye, 再见!']) + str(other_functions.f2_var)).upper())
    print_slow("                             --- by 2020 Jiaming & George")
    time.sleep(3)
  
    other_functions.first_option()

  elif logged_in_option1 == 'm':
    other_functions.Message_option()

  elif logged_in_option1 == 'g':
    Setting.entered_setting()

  elif logged_in_option1 == 's':
    print_slow("Coming soon!")
    try:
      Search_engine.entered_search()
    except:
      pass

terms_and_conditions = '''
----------------------------------------------------------------
Hello, SpyderChatter:
  
  Everytime you are using Spyderchat, you are automatically agreed to the following terms and conditions. If you do not agree, please delete your account right away.

  Spyderchat is a socialing tool that combines the functions of chatting, gaming, posting and others. Every material published by other users on this platform is not garanteed to be accutrate nor appropriate since spyderchat do not infiltrate into anyone's account in such context.

  We treat your privacy very seriously. The thing you are using now is designed ot be safe and lock your privacy only in you. We do not share your any private information with anyone without your permission. 

  If there are disputes over the above terms, Spyderchat team holds the ultimate authority of rights.

Enjoy SpyderChat!
                                    -------- Admin1 and Admin2
                                               2020 SpyderChat
'''