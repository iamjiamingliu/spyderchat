from py_folder import advanced_functions, forums, log_in, Messages_class, other_functions, Posts_class, Search_engine, Setting, SpyderChat, word_list

import pickle
from validate_email import validate_email

import os
import pickle
import arrow
import time
import random
import datetime
accounts_dictionary = {}
import math
def remove1(string): 
    return string.replace(" ", "") 

    
def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')



year1 = datetime.datetime.today().year
def is_valid_birthday(birthday: str):
  if len(birthday) >= 10:
    if birthday[2] == birthday[5] == '-':
      if int(birthday[:2]) > 0 and int(birthday[:2]) <= 12:
        if int(birthday[3:5]) > 0 and int(birthday[3:5]) < 32:
          if int(birthday[-4:]) > 1800 and int(birthday[-4:]) < int(year1):
            return True
  return False



def greeting():
  print('''Welcome to SpyderChat Developed by George and Jiaming!
  ''') 


class SpyderChatAccount():
    def __init__(self, username, real_name, email, phone_number, dob, gender, age, hobby, personal_comments, password):
        self.username = str(username)
        self.real_name = str(real_name)
        self.email = str(email)
        self.phone_number = str(phone_number)
        self.dob = str(dob)
        self.gender = str(gender)
        self.age = str(age)
        self.hobby = str(hobby)
        self.personal_comments = str(personal_comments)
        self.password = str(password)
    
    def get_info(self):
      infos = '''
      -----------------------------------------
      Username: %s        
      Realname: %s
      Date of Birth: %s
      Gender: %s
      Age: %s
      Hobby: %s
      Biography: %s
      -----------------------------------------
      ''' %(self.username, self.real_name, self.dob, self.gender, self.age, self.hobby, self.personal_comments)
      return infos
      


def exit1():
    aaaaa = open("central_db_folder/AV.txt","rb")
    aaaaa.close()
    print('''
    --------------------------------------------
    ''')
    print('               ' + random.choice(['Have a nice day!', 'Great! See you later!', 'Goodbye!', 'Bye-bye, Adios!', 'Bye-bye, 再见!']).upper())
    print("                             --- by 2020 Jiaming & George")
    time.sleep(4)
    clear()
    exit()
    

file_path = 'central_db_folder/AV.txt'

def create_account(a: dict):
    if os.stat(file_path).st_size != 0:
      a = pickle.load(open("central_db_folder/AV.txt","rb"))
    
    print('''
  -----------------------------------------------
  Ok, now you are creating your account. 
  Please follow the follwing instructions carefully.
  ''')
    
    time.sleep(3)
    clear()
    input_username = remove1(str(input('''
  -----------------------------------------------
  Please enter the username you want to use 
  (between 5 - 11 characters long): 
  ''')).lower())

    while len(input_username) > 11 or len(input_username) < 5 or input_username in a.keys():
      input_username = remove1(str(input('''
    --------------------------------------------
    Sorry, please enter something between 5 - 11 characters long! 
    Or, perhaps this username already exists! 
    Try a new one: 
    ''')).lower())

    input_real_name = str(input('''
  -----------------------------------------------
  Please enter your real name
  (If you incorrectly entered this information, 
  you might not be able to access some SpiderChat's functions): 
  '''))
  
    input_email = remove1(str(input('''
  -----------------------------------------------
  Please provide your email
  (This will be used to retrieve your password)
  (We will not reveal your email address to anyone):
  ''')))

    while validate_email(str(input_email)) == False:
      input_email = remove1(str(input('''
    -----------------------------------------------
    Please provide your TRUE email, not a fake one
    We take care your privacy very seriously, if you dont' enter your ture email, your account is at risk of lost
    Enter again:
  ''')))

    input_phone_number = str(input('''
    --------------------------------------------
  Please provide your phone number
  (This will be used to retrieve your password)
  (We will not reveal your phone number to anyone):
  '''))

    input_dob = str(input('''
  -----------------------------------------------
  Please enter your birthday (format: month-date-year) 
  If you incorrectly entered this information, 
  you might not be able to access some SpiderChat's functions: 
  ''')).lower()

    while is_valid_birthday(input_dob) == False:
      input_dob = str(input('''
    -----------------------------------------------
    Sorry, Please follow the proper format!
    If the date and month is less than 10, put a 0 in front
    example: enter 07-08-2005 for July 8th 2005 
    Enter Again: 
  ''')).lower()


    input_gender = str(input('''
  -----------------------------------------------
  Please enter your gender (male or female or NA)
  If you incorrectly entered this information, 
  you might not be able to access some SpiderChat's functions: 
  ''')).lower()

    while input_gender not in ['male', 'female', 'na']:
        input_gender = str(input('''
    -----------------------------------------------
    Sorry, you only enter male or female or NA please! 
    Try again: ''')).lower()


    input_age = remove1(str(input('''
  -----------------------------------------------
  Please enter your age 
  (If you incorrectly entered this information, 
  you might not be able to access some SpiderChat's functions:) 
  ''')).lower())
    while input_age not in [str(x) for x in range(200)]:
        input_age = remove1(str(input('''
    -----------------------------------------------
    Sorry, only enter a valid age in integer!
    Try again: 
    ''')))
    
    today = str(arrow.now().format('YYYY-MM-DD'))

    age1 = int(today[:4]) - int(input_dob[-4:])

    if int(input_age) not in [age1 - 1, age1, age1  + 1]:
      input_age = remove1(str(input('''
      -----------------------------------------------
      Sorry, your age does not correlate to your birthday!
      Try again: 
    ''')))



    input_hobby = str(input('''
  -----------------------------------------------
  Please describe your hobby: 
  '''))

    while len(input_hobby) >= 1000:
        input_hobby = str(input('''
    ----------------------------------------------
    Sorry, please enter less than 1000 characters!
    Please describe your hobby again: 
    '''))

    input_personal_comments = str(input('''
  -----------------------------------------------
  Write something about you!
  What do you want to say in your bio: 
  '''))
    while len(input_personal_comments) >= 1000:
        input_personal_comments = str(input('''
    -----------------------------------------------
    Sorry, please enter less than 1000 characters!
    Please describe your words again: 
    '''))

    input_password = remove1(str(input('''
  -----------------------------------------------
  Now, set a password for your account with username,
  %s :
  ''' %(input_username)).lower()))

    while len(input_password) < 5 or len(input_password) >30:
        input_password = str(input('''
    -----------------------------------------------
    Sorry, please enter something between 5 - 30 characters long!
    Try a new one: 
    ''')).lower()


    print('''
  -----------------------------------------------
  The valid password you entered is:''')
    print(input_password)
    print('and your username is:')
    print(input_username)
    print("Please do not reveal your password to anyone!\n")

    new_account = SpyderChatAccount(input_username, input_real_name, input_email, input_phone_number, input_dob, input_gender, input_age, input_hobby,
                                    input_personal_comments, input_password)

    a.update({new_account.username: new_account})
    

    pickle.dump(a, open("central_db_folder/AV.txt","wb"))

    new_file_name = 'z_folder/z_' + str(input_username) + ".db"

    Personal_messages_dict = {"Inbox":{}, "Sent":{}, "Drafts": {}}

    personal_info_dict = {"Messages": Personal_messages_dict, "Posts&Friends": {"Posts": {}, "Friends": [input_username]}, "Chats&Forums": {"Chats": None, "Forums":{"as_owner": {}, "as_participant": {}}},"Setting": new_account}

    pickle.dump(personal_info_dict, open(new_file_name, "wb"))

    log_in.foreverAV = a

    x1932 = open("Admin_folder/ZZZZAV.db","wb")

    if len(log_in.foreverAV.keys()) > 0 :
      pickle.dump(log_in.foreverAV, x1932)

    x1932.close()

    print('''
  -----------------------------------------------

  This is fantastic! 
  CONRADULATION, YOU ARE ALL SET FOR YOUR ACCOUNT!
  Spyderchat is taking you back...
  Or, Press "Run" on repl.it
  ''')
    time.sleep(3)
    clear()
    other_functions.first_option()










