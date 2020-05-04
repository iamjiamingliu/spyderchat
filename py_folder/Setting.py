from py_folder import advanced_functions, forums, log_in, Messages_class, other_functions, Posts_class, Search_engine, Setting, SpyderChat, word_list

import pickle
from validate_email import validate_email
import os

import time
from py_folder import Games_folder

import arrow


def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')


def entered_setting():
  clear()
  print("here is your public account information: ") 
  time.sleep(0.5)
  print(SpyderChat.accounts_dictionary[other_functions.f2_var].get_info())
  time.sleep(1)
  print('''
  -------------------------------------------------
  Here is your private information (only used to retreive your password when neccesary):
  ''')
  time.sleep(0.5)

  print("   password:  " + SpyderChat.accounts_dictionary[other_functions.f2_var].password)
  print("")
  print("   Email:  " + str(SpyderChat.accounts_dictionary[other_functions.f2_var].email))
  print("")
  print("   Phone Number: " + str(SpyderChat.accounts_dictionary[other_functions.f2_var].phone_number))
  print("")
  setting_option()

def setting_option():
  option1 = str(input('''
  -------------------------------------------------
  [G]ames     [C]hange information    [B]ack
  [D]elete Account    [S]ee Terms and Conditions    
  [H]elp
  ''')).lower()

  while option1 not in ['h','c','s','b','d', 'g']:
    option1 = str(input('''
    -------------------------------------------------
    Sorry, only choose one of the following!
    [C]hange information  [H]elp    [D]elete Account
    [S]ee Terms and Conditions      [G]ames
    [B]ack
  ''')).lower()

  if option1 == 'g':
    game_option = str(input('''
    -------------------------------------------------
    Would you like to play:
    [H]angman    [Z]ortho's Doungeon   [B]lack Jack
    [T]ic Tac Toe Double Player         or  [E]xit?
    ''')).lower()
    if game_option not in ['h', 'b','z','t', 'e']:
      setting_option()
    if game_option == 'e':
      setting_option()
    if game_option == 't':
      Games_folder.lore_game.play_tic_tac_toe()
      other_functions.clear()
      setting_option()
    if game_option == 'h':
      Games_folder.hangman.play_hangman()
      other_functions.clear()
      entered_setting()

    if game_option == 'b':
      Games_folder.blackjack.play_blackjack()
      other_functions.clear()
      entered_setting()

    if game_option == 'z':
      Games_folder.lore_game.opening()
      while input("Play Again? [Y/N] ").lower() == 'y':
        Games_folder.lore_game.opening() 
      print("Ok, hopefully you enjoyed!")
      time.sleep(2)
      clear()
      entered_setting()

      
      

  if option1 == 'h':
    print(log_in.User_manual)
    time.sleep(4)

  if option1 == 'b':
    log_in.second_option()

  if option1 == 's':
    print(log_in.terms_and_conditions)
    time.sleep(4)

  if option1 == 'd':
    delete_account()

  if option1 == 'c':
    change_account_info()

  stop = input("Enter nothing to go back to Setting")
  clear()
  setting_option()




def delete_account():
  option1 = input('''You sure you want to delete your account, %s? Once you delete, everything is gone. You sure? [Y/N]''' %(other_functions.f2_var)).lower()

  if option1 == 'y':
    av = pickle.load(open("central_db_folder/AV.txt", "rb"))
    name = av[other_functions.f2_var].real_name
    del av[other_functions.f2_var]
    pickle.dump(av, open("central_db_folder/AV.txt", "wb"))
    os.remove("z_folder/z_" + other_functions.f2_var + ".db")
    print("Ok, your account has been deleted... Spyderchat welcomes you back at anytime! Farefell %s" %(name))
    time.sleep(5)
    other_functions.first_option()

  else:
    print(":)")
    time.sleep(1.5)
    print("ok, good to hear that you are not deleting your account. ")

  
def change_account_info():
  all_dict = pickle.load(open("central_db_folder/AV.txt", "rb"))
  personal_dict = pickle.load(open("z_folder/z_" + other_functions.f2_var + ".db", "rb"))
  
  print('''
  -------------------------------------------------
  Ok, now you are changing your account.")

  Please follow the instructions carefully.
  If there are info you dont what to change, enter
  Nothing!''')
  time.sleep(3)

  print("Username (unchancheable): " + other_functions.f2_var)
  time.sleep(1.5)

  real_name1 = str(input('''
  -------------------------------------------------
  Your current Real Name is: %s
  If you want to change it, Enter the new one, or 
  enter nothing:
  ''' %(all_dict[other_functions.f2_var].real_name)))

  if real_name1 in ['',' ','   ']:
    real_name1 == all_dict[other_functions.f2_var].real_name

  email1 =  str(input('''
  -------------------------------------------------
  Your current Email is: %s
  If you want to change it, Enter the new one, or 
  enter nothing:
  ''' %(all_dict[other_functions.f2_var].email)))

  if email1 in ['','  ','   ']:
    email1 = all_dict[other_functions.f2_var].email


  phone1 =  str(input('''
  -------------------------------------------------
  Your current Phone Number is: %s
  If you want to change it, Enter the new one, or 
  enter nothing:
  ''' %(all_dict[other_functions.f2_var].str(phone_number))))

  if phone1 in ['','  ','   ']:
    phone1 = all_dict[other_functions.f2_var].phone_number


  dob1 =  str(input('''
  -------------------------------------------------
  Your current Birthday is: %s
  If you want to change it, Enter the new one, or 
  enter nothing:
  ''' %(all_dict[other_functions.f2_var].dob)))

  if dob1 in ['','  ','   ']:
    dob1 = all_dict[other_functions.f2_var].dob

  while SpyderChat.is_valid_birthday(dob1) == False:
        dob1 = str(input('''
      -----------------------------------------------
      Sorry, Please follow the proper format!
      If the date and month is less than 10, put a 0 in front
      example: enter 07-08-2005 for July 8th 2005 
      Enter Again: 
    ''')).lower()

  today = str(arrow.now().format('YYYY-MM-DD'))

  age1 = int(today[:4]) - int(dob1[-4:])

  hobby1 = str(input('''
  -------------------------------------------------
  What are your hobbies:
  If you want to change it, Enter the new one, or 
  enter nothing:
  '''))

  if hobby1 in ['','  ','   ']:
    hobby1 = all_dict[other_functions.f2_var].hobby


  bio1 = str(input('''
  -------------------------------------------------
  What do you want to put in your bio:
  If you want to change it, Enter the new one, or 
  enter nothing:
  '''))

  if bio1 in ['','  ','   ']:
      bio1 = all_dict[other_functions.f2_var].personal_comments
  
  password1 = str(input('''
  -------------------------------------------------
  Do you want to change your current password,
  %s ?
  If you want to change it, Enter the new one, or 
  enter nothing:
  ''' %(all_dict[other_functions.f2_var].password)))

  if password1 in ['','  ','   ']:
      password1 = all_dict[other_functions.f2_var].password

  gender = str(input('''
  -------------------------------------------------
  Your current gender = %s
  Would you like to change it to 
  [M]ale, [F]emale, or [N]A?
  ''' %(all_dict[other_functions.f2_var].gender))).lower()
  
  while gender not in ['m', 'f', 'n', '',]:
        gender = str(input('''
    -----------------------------------------------
    Sorry, you only enter M or F or N please! 
    Try again: ''')).lower()
  
  gender = {"": all_dict[other_functions.f2_var].gender, "m":"male", "f":"female", "n":"NA"}[gender]
  
  new_object = SpyderChat.SpyderChatAccount(other_functions.f2_var, real_name1, email1, phone1, dob1, gender, age1, hobby1, bio1, password1)

  all_dict.update({other_functions.f2_var: new_object})
  
  other_functions.Accountdb = all_dict
  SpyderChat.accounts_dictionary = all_dict
  other_functions.f1_var = all_dict

  pickle.dump(all_dict, open("central_db_folder/AV.txt", "wb"))

  personal_file = 'z_folder/z_' + other_functions.f2_var +'.db'

  per_file_setting_object = pickle.load(open(personal_file, "rb"))

  per_file_setting_object.update({"Setting":new_object})

  pickle.dump(per_file_setting_object, open(personal_file, "wb"))

  print('''
  ___________________________________________________
  Congradulation! You are all set for a brand new you!
  ''')
  time.sleep(1)
  entered_setting()

