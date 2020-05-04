from py_folder import advanced_functions, forums, log_in, Messages_class, other_functions, Posts_class, Search_engine, Setting, SpyderChat, word_list

import pickle
from validate_email import validate_email
import os
import pickle

import time

import arrow
import math
Accountdb = {}

f1_var = {}

f2_var = str()
all_users = []
vall_users = []

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')


def first_option():
    clear()
    option1 = str(input('''
 -----------------------------------------------
 Would you like to:
 [L]ogin
 [C]reate New Account
 [E]xit
 ''')).lower()

    while option1 not in ['l', 'e', 'c']:
        option1 = str(input('''
 -----------------------------------------------
 Sorry, only enter L or C or E !
 Press:
 [L]ogin
 [C]reate New Account
 [E]xit
 ''')).lower()

    if option1 == 'l':
        cur_username = log_in.log_in1()
        global f2_var
        f2_var = cur_username
        log_in.logged_in(cur_username)
        pass

    elif option1 == 'c':
        SpyderChat.create_account(f1_var)
        first_option
    elif option1 == 'e':
        SpyderChat.exit1()


def Message_option_without():
    clear()
    cur_username = 'z_folder/z_' + f2_var + ".db"
    a = open(cur_username, "rb")
    personal_dict = pickle.load(a)
    Messages_section = personal_dict["Messages"]
    print('''
-------------------------------------------------------
Inbox:
ID   |   Date    |  Sender  |   Subject   |     Content
 ''')

    if len(Messages_section["Inbox"]) != 0 and len(Messages_section["Inbox"]) < 7:
        for key, item in list(Messages_section["Inbox"].items())[::-1]:
            print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                  item.content[:15] + '...')

    if len(Messages_section["Inbox"]) >=  7:
        limit = 7
        cur_limit = 1
        used_items = []
        print("   You have a lot of emails. Here are your unreads")
        time.sleep(1)
        for key, item in list(Messages_section["Inbox"].items())[::-1]:

            if (cur_limit < limit) and item.is_checked() == False:
                print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                      item.content[:15] + '...')
                used_items.append(item)
                cur_limit += 1

        if len(used_items) != len(list(Messages_section["Inbox"].items())):
              more = str(input('''
              ----------------------------------
              [M]ore, or Enter nothing to Continue: ''')).lower()

        while (more == 'm' and len(used_items) != len(list(Messages_section["Inbox"].items()))):
            limit += 7
            for key, item in list(Messages_section["Inbox"].items())[::-1]:
                if (item not in used_items) and (cur_limit < limit):
                    print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                          item.content[:15] + '...')
                    cur_limit += 1
                    used_items.append(item)

                if len(used_items) == len(list(Messages_section["Inbox"].items())):
                    
                    break
            if len(used_items) != len(list(Messages_section["Sent"].items())):
              more = str(input('''
              ----------------------------------
              [M]ore, or Enter nothing to Continue: ''')).lower()

    else:
        print('''
     That is all the mails you have In Inbox ''')
        time.sleep(1)

    print('''
-------------------------------------------------------
Sent:
ID   |   Date    |  Sender  |   Subject   |     Content
 ''')

    if len(Messages_section["Sent"]) != 0 and len(Messages_section["Sent"]) < 7:
        for key, item in list(Messages_section["Sent"].items())[::-1]:
            print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                  item.content[:15] + '...')

    if len(Messages_section["Sent"]) >=  7:
        limit = 7
        cur_limit = 1
        used_items = []
        print("   You have a lot of Sents. Here are some of them:")
        time.sleep(1)
        for key, item in list(Messages_section["Sent"].items())[::-1]:
            if (cur_limit < limit) and item.is_checked() == False:
                print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                      item.content[:15] + '...')
                used_items.append(item)
                cur_limit += 1

        if len(used_items) != len(list(Messages_section["Inbox"].items())):
              more = str(input('''
              ----------------------------------
              [M]ore, or Enter nothing to Continue: ''')).lower()
        while (more == 'm' and len(used_items) != len(list(Messages_section["Sent"].items()))):
            limit += 7
            if cur_limit < limit:
              for key, item in list(Messages_section["Sent"].items())[::-1]:
                  if (item not in used_items) and cur_limit < limit:
                      print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                            item.content[:15] + '...')
                      cur_limit += 1
                      used_items.append(item)

            if len(used_items) == len(list(Messages_section["Sent"].items())):
                
                break
            if len(used_items) != len(list(Messages_section["Sent"].items())):
              more = str(input('''
              ----------------------------------
              [M]ore, or Enter nothing to Continue: ''')).lower()


    else:
        print('''
      That is all the mails you have in Sent section ''')
        time.sleep(1)
    optionx1()


def Message_option():
    clear()
    cur_username = 'z_folder/z_' + f2_var + ".db"
    a = open(cur_username, "rb")
    personal_dict = pickle.load(a)
    Messages_section = personal_dict["Messages"]
    print('''
-------------------------------------------------------
Inbox:
ID   |   Date    |  Sender  |   Subject   |     Content
 ''')

    if len(Messages_section["Inbox"]) != 0 and len(Messages_section["Inbox"]) < 7:
        for key, item in list(Messages_section["Inbox"].items())[::-1]:

            print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                  item.content[:15] + '...')
            time.sleep(0.6)

    if len(Messages_section["Inbox"]) >=  7:
        limit = 7
        cur_limit = 1
        used_items = []
        print("   You have a lot of emails. Here are your unreads")
        time.sleep(1)

        for key, item in list(Messages_section["Inbox"].items())[::-1]:
            if (cur_limit < limit) and item.is_checked() == False:
                print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                      item.content[:15] + '...')
                used_items.append(item)
                cur_limit += 1
                time.sleep(0.4)

        if len(used_items) != len(list(Messages_section["Inbox"].items())):
              more = str(input('''
              ----------------------------------
              [M]ore, or Enter nothing to Continue: ''')).lower()
        while (more == 'm' and len(used_items) != len(list(Messages_section["Sent"].items()))):
            limit += 7
            for key, item in list(Messages_section["Inbox"].items())[::-1]:
                if item not in used_items and (cur_limit < limit):
                    print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                          item.content[:15] + '...')
                    used_items.append(item)
                    time.sleep(0.4)
                    cur_limit += 1
                
            if len(used_items) != len(list(Messages_section["Inbox"].items())):
              more = str(input('''
              ----------------------------------
              [M]ore, or Enter nothing to Continue: ''')).lower()
            break

    print('''
     That is all the mails you have In Inbox ''')
    
    try:
      time.sleep(1 +int(math.log(len(list(Messages_section["Inbox"].items())))))
    except:
      pass
    print('''
-------------------------------------------------------
Sent:
ID   |   Date    |  Sender  |   Subject   |     Content
 ''')

    if len(Messages_section["Sent"]) != 0 and len(Messages_section["Sent"]) < 7:
        for key, item in list(Messages_section["Sent"].items())[::-1]:
            print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                  item.content[:15] + '...')
            time.sleep(0.6)

    if len(Messages_section["Sent"]) >=  7:
        limit = 7
        cur_limit = 1
        used_items = []
        print("   You have a lot of Sents. Here are some of them:")
        time.sleep(1.5)
        for key, item in list(Messages_section["Sent"].items())[::-1]:
            if cur_limit < limit:
                print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                      item.content[:15] + '...')
                cur_limit += 1
                used_items.append(item)
                time.sleep(0.4)

        if len(used_items) != len(list(Messages_section["Sent"].items())):
              more = str(input('''
              ----------------------------------
              [M]ore, or Enter nothing to Continue: ''')).lower()
        while (more == 'm' and len(used_items) != len(list(Messages_section["Sent"].items()))):
            limit += 7
            for key, item in list(Messages_section["Sent"].items())[::-1]:
                if item not in used_items and cur_limit < limit:
                    print(item.ID, ' ', item.sent_date, ' ', item.sender, ' ', item.subject[:8] + '...', ' ',
                          item.content[:15] + '...')
                    cur_limit += 1
                    used_items.append(item)
                    time.sleep(0.4)
            if len(used_items) == len(list(Messages_section["Sent"].items())):
               
                break
            if len(used_items) != len(list(Messages_section["Sent"].items())):
              more = str(input('''
              ----------------------------------
              [M]ore, or Enter nothing to Continue: ''')).lower()


    else:
        print('''
      That is all the mails you have in Sent section ''')
        time.sleep(1)
  
    try:
      time.sleep(1 +int(math.log(len(list(Messages_section["Sent"].items())))))
    except:
      pass
    optionx1()



def optionx1():
    readingID = ''
    cur_username = 'z_folder/z_' + f2_var + ".db"
    a = open(cur_username, "rb")
    personal_dict = pickle.load(a)
    Messages_section = personal_dict["Messages"]

    optionx = SpyderChat.remove1(str(input('''
---------------------------------------------------------
[B]ack    [H]elp   [N]ew Message   [D]rafts
or Enter the Message ID
ex: 1010 to check that specific email:
 ''')).lower())

    valid_list = [str(x) for x in range(999, 99999)]
    xx123 = valid_list + ['b', 'h', 'n', 'd']

    while optionx not in xx123:
        optionx = str(input('''
  ---------------------------------------------------------
  Sorry, please enter a valid option!
  [B]ack    [H]elp   [N]ew Message   [D]rafts
  or Enter the Message ID
  ex: 1010 to check that specific email:
  ''')).lower()

    if optionx == 'b':
        log_in.second_option()

    elif optionx == 'n':
        Messages_class.new_message()
        log_in.second_option()

    elif optionx == 'd':
        Messages_class.see_drafts()
        optionx1()

    elif optionx == 'h':
        print(log_in.User_manual)
        time.sleep(4)
        stop_reading = str(input(("Hit Enter to go back: ")))
        while stop_reading not in ['', ' ', '   ', '    ']:
            stop_reading = str(input(("Hit Enter to go back: ")))
        Message_option_without()
    elif optionx in valid_list:
        if int(optionx) not in Messages_section["Inbox"].keys() and int(optionx) not in Messages_section["Sent"].keys():
            print("Sorry, ID not found!")
            time.sleep(1.5)
            optionx1()

        if int(optionx) in Messages_section["Inbox"].keys():
            print(' ok, now you are seeing message with ID' + optionx + '')
            time.sleep(1.5)
            clear()
            print(Messages_section["Inbox"][int(optionx)].View_message())
            try:
              Messages_section["Inbox"][int(optionx)].view_reply()
            except:
              print("Sorry, this message is sent before SpyderChat version 0.02! We are unable to do it for you. ")
            Messages_section["Inbox"][int(optionx)].received_date = str(arrow.now().format('YYYY-MM-DD'))
            personal_dict.update({"Messages": Messages_section})
            pickle.dump(personal_dict, open(cur_username, "wb"))
            a.close()
            readingID = int(optionx)
            time.sleep(4)

        if int(optionx) in Messages_section["Sent"].keys():
            print(' ok, now you are seeing message with ID' + optionx + '')
            time.sleep(1.5)
            clear()
            print(Messages_section["Sent"][int(optionx)].View_message())
            try:
              Messages_section["Sent"][int(optionx)].view_reply()
            except:
              print("Sorry, this message is sent before SpyderChat version 0.02! We are unable to do it for you. ")
            readingID = int(optionx)
            time.sleep(4)

    stop_reading = str(input(('''
    -----------------------------------
    Hit Enter to go back, or 
    [R]eply or [D]elete this Message: 
    ''')))
    
    while stop_reading.lower() not in ['', ' ', 'r', 'd']:
      stop_reading = str(input(("Hit Enter or [R]eply: ")))

    if stop_reading in ['r','R']:
      try: 
        Messages_class.reply_message(readingID, Messages_section["Inbox"][int(optionx)].sender)
        
      except:
        print("Sorry, this message is sent before SpyderChat version 0.02! We are unable to do it for you. ")

    if (stop_reading in ['d','D'] and int(optionx) in Messages_section["Inbox"].keys()):
      print("You are deleting message with ID, " + str(readingID) +'')
      Messages_class.delete_message(f2_var, readingID, )
      time.sleep(1)
      print("Message Deleted!")
      time.sleep(1.5)

    if (stop_reading in ['d','D'] and int(optionx) in Messages_section["Sent"].keys()):
      print("Sorry, you can only delete message in your inbox, not retreive sent message!")
      time.sleep(2.5)

    Message_option_without()


def retreive_account(username):

  distance_limit = 6
  file_name = 'z_folder/z_' + str(username) + ".db"
  personal_dict = pickle.load(open(file_name, "rb"))
  print(personal_dict)
  setting_info = personal_dict["Setting"]
  print(setting_info)
  print(setting_info.phone_number)
  print(setting_info.email)
  print(setting_info.password)
  print(setting_info.dob)
  print(setting_info.real_name)
  print('''
  -------------------------------------------------
  Ok, you are retreiving your account with username,
  %s  Please follow the instructions carefully.''' %(username))
  time.sleep(5)
  #clear()

  input_password = str(input('''
  -------------------------------------------------
  Do you still remember some parts of your password?
  If you do, enter as many as you can here; otherwise 
  do not enter anything:
  ''')).lower()


  if len(input_password) != 0:
    distance_limit -=  advanced_functions.editDistDP(input_password, str(setting_info.password), len(input_password),len(setting_info.password))
    distance_limit += 2

  else:
    distance_limit -= 3

  input_email = str(input('''
  -------------------------------------------------
  Do you still remember the email you entered for your account?
  If you do, enter here; otherwise 
  do not enter anything:
  ''')).lower()

  if len(input_email) != 0:
    while SpyderChat.validate_email(input_email) == False:
        input_email = SpyderChat.remove1(str(input('''
      -----------------------------------------------
      Please provide your TRUE email, not a fake one
      We take care your privacy very seriously, if you dont' enter your ture email, your account is at risk of lost
      Enter again:
    ''')))

    distance_limit -=  advanced_functions.editDistDP(input_email, str(setting_info.email), len(input_email), len(str(setting_info.email)))
  
    distance_limit += 2

  if len(input_email) == 0:
    distance_limit -= 3

  input_phone_number = str(input('''
  -------------------------------------------------
  Do you still remember the phone number you entered for your account?
  If you do, enter here; otherwise 
  do not enter anything:
  ''')).lower()
  
  if len(input_phone_number) != 0:
    distance_limit -=  advanced_functions.editDistDP(input_phone_number, str(setting_info.phone_number), len(input_email), len(str(setting_info.phone_number)))
    distance_limit += 1
  
  if len(input_phone_number) == 0:
    distance_limit -= 2

  input_dob = str(input('''
  -------------------------------------------------
  Do you still remember the birth date you entered for your account?
  Please enter it regardlessly: (format: DD-MM-YYYY)
  ''')).lower()
  
  while SpyderChat.is_valid_birthday(input_dob) == False:
    input_dob = str(input('''
  -------------------------------------------------
  Sorry, please follow the format, DD-MM-YYYY
  :
  ''')).lower()
  
  distance_limit -=  advanced_functions.editDistDP(input_dob, str(setting_info.dob), len(input_dob), len(str(setting_info.dob)))

  distance_limit += 1
  
  if distance_limit >= 0:
    print('Congradulation! Your password is: ' + str(setting_info.password))
    time.sleep(4)
    if len(input("Enter anything to continue")) >=0:
      print("Please remember the password, we are taking you back...")
      time.sleep(3)
    return True
  
  else:
    print("Sorry, your account could not be retreived because you entered too many false information... try to create an account perhaps...")
    time.sleep(3)
    return False
