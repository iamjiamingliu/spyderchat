from py_folder import advanced_functions, forums, log_in, Messages_class, other_functions, Posts_class, Search_engine, Setting, SpyderChat, word_list


import pickle
from validate_email import validate_email
import os
import math
import pickle
import time
import random
import datetime

import arrow

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

class Messages():
  def __init__(self, sender, receivers, subject, content, sent_date, recieved_date, ID, reply):
    self.sender = str(sender).lower()
    self.receivers = list(receivers)
    self.subject = str(subject)
    self.content = str(content)
    self.sent_date = str(sent_date).lower()
    self.received_date = str(recieved_date).lower
    self.ID = int(ID)
    self.reply = {}


  def is_checked(self):
    return self.received_date != None 


  def send_message(content):
    for i in content.receivers:
      receiver_file_name = 'z_folder/z_' + str(i) + ".db"
      receiver_info = pickle.load(open(receiver_file_name, "rb"))
      receiver_info["Messages"]["Inbox"].update({int(content.ID):content})
      pickle.dump(receiver_info, open(receiver_file_name, "wb"))

    print('''
    --------------------------------------------------------
    You have successfully sent a message!
    ''') 
    aaabb = open(receiver_file_name,"rb")
    aaabb.close()
      

  def View_message(self):
    a = '''
    --------------------------------------------
    From: %s
    To: %s
    Subject: %s

    %s

    Message ID: %d
    --------------------------------------------
                                %s4-0[[-zCX]]
    ''' % (self.sender, str(self.receivers), self.subject, self.content, self.ID, self.sent_date)

    return a

  def view_reply(self):
    if len(self.reply) > 0:
      print("Here are the replies to this message: ")
      time.sleep(1.5)

      for ID1, item in list(self.reply): 
        print(item.View_message())
        time.sleep(1.5)

def reply_message(replyID: int, receiver: str):
  print("Ok, now you are replying to Message: " + str(replyID) + '')
  time.sleep(2)

  final_receivers = []
  final_receivers.append(receiver)

  taken_ID = int(pickle.load(open("central_db_folder/BiggestID.txt","rb")))

  ID1 = taken_ID + 2

  receiver_file_name = 'z_folder/z_' + str(receiver) + ".db"
  
  receiver_info = pickle.load(open(receiver_file_name, "rb"))
  
  
      
  pickle.dump(receiver_info, open(receiver_file_name, "wb"))
  
  subject1 = str('Reply to Your Message with ID ' + str(replyID) + '')

  content1 = str(input('''
  --------------------------------------------------
  Type your Message here:
  '''))


  today = str(arrow.now().format('YYYY-MM-DD'))

  pickle.dump(ID1, open("central_db_folder/BiggestID.txt","wb"))


  new_message_class_object = Messages(other_functions.f2_var, final_receivers, subject1, content1, today, None, ID1, [])


  try:
    receiver_info["Messages"]["Inbox"][replyID].reply.update({ID1: new_message_class_object})

  except:
    pass

  try:
    receiver_info["Messages"]["Sent"][replyID].reply.update({ID1: new_message_class_object})
    
  except:
    pass
  
  Messages.send_message(new_message_class_object)

  wi102 = open('z_folder/z_' + other_functions.f2_var + '.db', "rb")

  sent_dict = pickle.load(wi102)

  sent_dict["Messages"]["Sent"].update({new_message_class_object.ID: new_message_class_object})

  pickle.dump(sent_dict, open('z_folder/z_' + other_functions.f2_var + '.db', "wb"))

  wi102.close()

  print("You have succesfully replied to Message: " + replyID + '!')

  time.sleep(1)




def new_message():
  try:
    other_functions.all_users.remove("v")
  except:
    pass
  receiver_list = []
  sender  = 'z_folder/z_' + other_functions.f2_var + ".db"
  print('''
    Ok, now you are sending a new message. Please follow the instructions carefully
  ''')
  time.sleep(3)
  clear()
  receivers_input = SpyderChat.remove1(str(input('''
    --------------------------------------------------------
    Receiver:                                 or [B]ack
    '''
  )).lower())


  while receivers_input not in other_functions.all_users:
    receivers_input = SpyderChat.remove1(str(input('''
      --------------------------------------------------------
      Sorry, username does not exit!
      Try again or [B]ack:
  ''' )).lower())
    

    if receivers_input == 'b':
        print("Ok, taking you back...")
        time.sleep(2)
        other_functions.optionx1()

  receiver_list.append(receivers_input)
  
  try:
    other_functions.all_users.remove("v")
  except:
    pass

  while receivers_input != '':
    receivers_input = SpyderChat.remove1(str(input('''
    Who is next (if there is only one receiver, hit[Enter])
    or [B]ack to your mailbox:
  ''')).lower())
    if receivers_input == 'b':
      print("Ok, taking you back to your mailbox...")
      time.sleep(2)
      other_functions.optionx1()
    
    while receivers_input != '' and receivers_input not in other_functions.all_users:
      receivers_input = SpyderChat.remove1(str(input('''
      --------------------------------------------------------
      Sorry, username does not exit!
      Try again,
      or [B]ack to mailbox:    
      ''' )).lower())
      
      if receivers_input == 'b':
        print("Ok, taking you back to your mailbox...")
        time.sleep(2)
        other_functions.optionx1()


    receiver_list.append(receivers_input)

  final_receivers = [x for x in receiver_list if x in other_functions.f1_var.keys()]

  clear()

  subject1 = str(input('''
    --------------------------------------------------------
    Type your subject here:
    '''))

  content1 = str(input('''
    --------------------------------------------------------
    Type your message here:
  '''))

  
  today = str(arrow.now().format('YYYY-MM-DD'))

  taken_ID = int(pickle.load(open("central_db_folder/BiggestID.txt","rb")))

  ID1 = taken_ID + 2

  pickle.dump(ID1, open("central_db_folder/BiggestID.txt","wb"))


  new_message_class_object = Messages(other_functions.f2_var, final_receivers, subject1, content1, today, None, ID1, [])


  send1 = str(input("You sure you want to send? [Y/N] \n")).lower()
  
  if send1 != 'y':
    file_name = 'z_folder/z_' + str(other_functions.f2_var) + '.db'
    file_dict = pickle.load(open(file_name, "rb"))
    file_dict["Messages"]["Drafts"].update({new_message_class_object.ID: new_message_class_object})
    pickle.dump(file_dict, open(file_name, "wb"))
    print("Ok, your draft has been saved.")

    time.sleep(2)
    other_functions.Message_option_without()


  Messages.send_message(new_message_class_object)

  wi102 = open(sender, "rb")

  sent_dict = pickle.load(wi102)

  sent_dict["Messages"]["Sent"].update({new_message_class_object.ID: new_message_class_object})

  pickle.dump(sent_dict, open(sender, "wb"))

  wi102.close()

  pickle.dump(ID1, open("central_db_folder/BiggestID.txt","wb"))



def delete_message(user: str, readingID: int):
  deleter_file = open('z_folder/z_' + user +'.db', "rb")
  deleter_info = pickle.load(deleter_file)

  a = deleter_info

  del a["Messages"]["Inbox"][int(readingID)]

  pickle.dump(a, open('z_folder/z_' + user +'.db', "wb"))
  deleter_file.close()


def see_drafts():

  file_name = 'z_folder/z_' + str(other_functions.f2_var) + '.db'
  file_dict = pickle.load(open(file_name, "rb"))

  if len(file_dict["Messages"]["Drafts"]) == 0:
    print("Seems you have no drafts yet...")
    print("Taking you back...")
    time.sleep(2)
    other_functions.optionx1()

  print('''
  ------------------------------------------
  Ok, here are your drafts: ''')

  time.sleep(1.5)
  print('''
  Draft ID |  Subject  |       Content      |
  ''')

  if len(file_dict["Messages"]["Drafts"]) < 7:
    for key, i in file_dict["Messages"]["Drafts"].items():
      print('   ', i.ID, '   ', i.subject[:-8], '...','   ',i.content[:-10], '...')
      time.sleep(0.6)

  if len(file_dict["Messages"]["Drafts"]) >= 7:
    for key, item in list(file_dict["Messages"]["Drafts"].items())[-6:]:
      print('   ', i.ID, '   ', i.subject[:-8], '...','   ',i.content[:-10], '...')
      time.sleep(0.6)

  draft_option = str(input('''
  --------------------------------------------------
  [B]ack     or Enter the Message ID to view or send:
  ''')).lower()

  if draft_option == 'b':
    other_functions.Message_option_without()

  while int(draft_option) not in file_dict["Messages"]["Drafts"].keys():
    draft_option = str(input('''
  --------------------------------------------------
  Sorry, ID not found!
  [B]ack     or Enter the Message ID to view or send:
  ''')).lower()

  valid_list = [str(x) for x in range(999, 99999)]
  if draft_option in valid_list:
    print('''
    --------------------------------------------------
    Ok, you are viewing the Draft with ID, %s
    ''' %(draft_option))

    time.sleep(2)
    clear()

    print(file_dict["Messages"]["Drafts"][int(draft_option)].View_message())

    try:
      file_dict["Messages"]["Drafts"][int(draft_option)].view_reply()
    
    except:
      print("Sorry, this function is not supported...")

    send_option = str(input('''
    --------------------------------------------------
    [S]end or [D]elete this draft or [B]ack:
    ''')).lower()

    if send_option == 's':
      print("Ok, sending the message...")
      Messages.send_message(file_dict["Messages"]["Drafts"][int(draft_option)])
      
      file_dict["Messages"]["Sent"].update({int(draft_option):file_dict["Messages"]["Drafts"][int(draft_option)]})

      del file_dict["Messages"]["Drafts"][int(draft_option)]
      
      pickle.dump(file_dict, open(file_name, "wb"))

      time.sleep(1.5)
      other_functions.Message_option_without()


    if send_option == 'd':
      del file_dict["Messages"]["Drafts"][int(draft_option)]
      pickle.dump(file_dict, open(file_name, "wb"))
      print("Ok, draft deleted!")
      time.sleep(1)
      other_functions.Message_option_without()



  pickle.dump(file_dict, open(file_name, "wb"))


