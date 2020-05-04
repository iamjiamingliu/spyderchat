from py_folder import advanced_functions, forums, log_in, Messages_class, other_functions, Posts_class, Search_engine, Setting, SpyderChat, word_list

from validate_email import validate_email
import os
from termcolor import colored
import arrow
import math
import pickle
import time
import random


class Posts():
  def __init__(self, poster, content, date, up_votes, comments, ID, viewers):
    self.poster = str(poster)
    self.content = str(content)
    self.date = str(date)
    self.up_votes = int(up_votes)
    self.comments = list(comments)
    self.ID = int(ID)
    self.viewers = list(viewers)

  def view_post_general(self):
    view = str('''%d| %s: "%s"... %d Likes''' %(self.ID,self.poster, self.content[:20], self.up_votes))
    return view
  
  def view_post_specific(self):
    view = str('''
_____________________________________________________________

Your friend %s on %s posted:
    
    %s

-------------------------------------------------------------
  Comments:

    %s
  
  %d Likes                            Post ID: %d
    ''' %(self.poster, self.date, self.content, self.comments[::-1], self.up_votes, self.ID))
    return view
  def delete_post(self):
    personal_dict = pickle.load(open("z_folder/z_"+ other_functions.f2_var + ".db", "rb"))
    if personal_dict["Posts&Friends"]["Posts"][int(self.ID)].poster == other_functions.f2_var:
      for i in personal_dict["Posts&Friends"]["Friends"]:
        friend_dict = pickle.load(open('z_folder/z_' + i + '.db', "rb"))
        friend_dict["Posts&Friends"]["Posts"][int(self.ID)].content = "The user has deleted this post"
        friend_dict["Posts&Friends"]["Posts"][int(self.ID)].up_votes = 0
        friend_dict["Posts&Friends"]["Posts"][int(self.ID)].comments = ["The user has deleted this post"]

        pickle.dump(friend_dict, open('z_folder/z_' + i + '.db', "wb"))

    try:
      del personal_dict["Posts&Friends"]["Posts"][int(self.ID)]
    except:
      pass
    pickle.dump(personal_dict, open("z_folder/z_"+ other_functions.f2_var + ".db", "wb"))
    print("OK, you have succesfully deleted the  post!")
  

def create_post():
  print('''
  _________________________________________
  Ok, now you are creating a new post. 
  Please follow the instructions carefully''')
  time.sleep(2)
  other_functions.clear()
  
  input_content = str(input('''
  ___________________________________________
  Please enter the content you want to post:
  ''')).lower()



  input_poster = str(other_functions.f2_var)
  input_date = str(arrow.now().format('YYYY-MM-DD'))
  
  input_ID = int(pickle.load(open("central_db_folder/BiggestID.txt", "rb")))
  input_ID += 1

  pickle.dump(int(input_ID + 1), open("central_db_folder/BiggestID.txt", "wb"))



  new_post_object = Posts(input_poster, input_content, input_date, 1, ["Nothing yet at this point"], input_ID, pickle.load(open("z_folder/z_" + other_functions.f2_var + ".db", "rb"))["Posts&Friends"]['Friends'])
  
  for friend in new_post_object.viewers:
    friend_file = "z_folder/z_" + friend + ".db"
    friends_dict = pickle.load(open(friend_file, "rb"))
    friends_dict["Posts&Friends"]["Posts"].update({input_ID: new_post_object})
    pickle.dump(friends_dict, open(friend_file, "wb"))

  print("Success!")
  time.sleep(1.5)

def post_menu():
    personal_dict = pickle.load(open("z_folder/z_" + other_functions.f2_var + ".db", "rb"))
    personal_posts = personal_dict["Posts&Friends"]["Posts"]
    used_items = []
    limit = 6
    cur = 1
    other_functions.clear()
    print(colored('''
  ___________________________________________________
  Here are the new posts: 
  ''', "yellow"))

    time.sleep(2)
    
    if len(personal_posts.keys()) == 0:
      print("You have nothing yet! ")
      time.sleep(1.5)
      menu_choice()

    while (cur < limit and len(used_items) != list(personal_posts.items())):
      for key, item in list(personal_posts.items())[::-1]:
        if cur == limit:
          more = str(input('[M]ore, or [Enter] to skip  ')).lower()
          if more == 'm':
            limit += 6
            continue
          if more != 'm':
            break
            menu_choice()
        if item not in used_items:
          print(colored(('   ' + item.view_post_general()), "yellow"))
          time.sleep(0.4)
          used_items.append(item)
          cur += 1

      if len(used_items) == len(list(personal_posts.keys())):
        print("           That is all the post you have!")
        time.sleep(1)
        menu_choice()
      


    menu_choice()

def menu_choice():
  personal_dict = pickle.load(open("z_folder/z_" + other_functions.f2_var + ".db", "rb"))
  personal_posts = personal_dict["Posts&Friends"]["Posts"]
  
  post_choice = str(input('''
  ___________________________________________________
  [N]ew Posts    [F]riends    [B]ack       or
  Enter the Post ID to View the specific Post:
  ''')).lower()
  all_keys = [str(i) for i in personal_posts.keys()]
  all_keys.append('n')
  all_keys.append('b')
  all_keys.append('f')
  while post_choice not in all_keys:
    post_choice = str(input('''
    ___________________________________________________
    Sorry, only enter on of the following!
    [N]ew Posts    [F]riends    [B]ack     or
    Enter the Post ID to View the specific Post:
    ''')).lower()
  if post_choice == 'b':
    log_in.second_option()

  elif post_choice == 'n':
    create_post()
    time.sleep(2)
    post_menu()

  elif post_choice == 'f':
    view_friends_general()
    time.sleep(2)
    post_menu()

  elif int(post_choice) in personal_posts.keys():
    print("Ok, now you are viewing the post with ID, %s" %(post_choice))
    time.sleep(2)
    other_functions.clear()
    print(personal_posts[int(post_choice)].view_post_specific())
    specific_option = str(input('''
        _______________________________________________
            [C]omment   [L]ike this Post    [B]ack
            ''')).lower()
    if specific_option == 'c':
      input_comment = str(input("Enter your comment here: \n"))
      viewers1 = personal_posts[int(post_choice)].viewers
      for viewer in viewers1:
        view_dict = pickle.load(open("z_folder/z_" + viewer + ".db", "rb"))
        view_dict["Posts&Friends"]["Posts"][int(post_choice)].comments.append(input_comment)
        pickle.dump(view_dict, open("z_folder/z_" + viewer + ".db", "wb"))
      print("Success!")
      time.sleep(1.5)
      post_menu()
            
    if specific_option == 'l':
      viewers1 = personal_posts[int(post_choice)].viewers
      for viewer in viewers1:
        view_dict = pickle.load(open("z_folder/z_" + viewer + ".db", "rb"))
        view_dict["Posts&Friends"]["Posts"][int(post_choice)].up_votes += 1
        pickle.dump(view_dict, open("z_folder/z_" + viewer+ ".db", "wb"))
      print("Success!")
      time.sleep(1.5)
  
      post_menu()
        



  post_menu()


def view_friends_general():
  personal_dict = pickle.load(open("z_folder/z_" + other_functions.f2_var + ".db", "rb"))
  other_functions.clear()
  print('''
  _______________________________________
  Here are your Friends:
  ''')
  time.sleep(1.5)
  limit = 6
  cur = 1
  used = []
  for i in personal_dict["Posts&Friends"]["Friends"][::-1]:
    if cur == limit:
      more = str(input("load [M]ore, or [Enter] to continue: "))
      if more.lower() == 'm':
        cur += 6
        continue
      else:
        break
    print('    '+i)
    used.append(i)
    cur += 1
    time.sleep(0.4)
    
    if len(used) == len(personal_dict["Posts&Friends"]["Friends"]):
      print("That is all of your friends. ")
      time.sleep(2)
      friend_choice()
    
    

def friend_choice():
  choicefriend = str(input('''
  _________________________________________
  [B]ack  [V]iew Friend Suggestions  
  or Enter a username to view friend profile
  ''')).lower()
  possibles = ['b','v','a']
  possibles = possibles + other_functions.vall_users
  while choicefriend not in possibles:
    choicefriend = str(input('''
    _________________________________________
    Sorry, only enter a valid option!
    [B]ack  [V]iew Friend Suggestions 
    or Enter a username to view friend profile
  ''')).lower()

  if choicefriend == 'b':
    post_menu()

  if choicefriend == 'v':
    view_suggestions_general()

  if choicefriend in other_functions.vall_users:
    print("Ok, here is your friend, " + choicefriend)
    time.sleep(2)
    other_functions.clear()
    friend_dict1 = pickle.load(open("z_folder/z_" + choicefriend + ".db", "rb"))
    print(colored(friend_dict1["Setting"].get_info(), "yellow"))
    time.sleep(2)
    
    specific_friend_option = str(input('''
    ______________________________________________
    [B]ack    [S]end him/her a message  [U]nfriend
    ''')).lower()

    while specific_friend_option not in ['u','s','b']:
      specific_friend_option = str(input('''
      ______________________________________________
      Sorry, please enter a valid option!
      [B]ack    [S]end him/her a message  [U]nfriend
    ''')).lower()

    if specific_friend_option == 'b':
      print("OK, taking you back...")
      time.sleep(1.5)
      other_functions.clear()
      view_friends_general()
    if specific_friend_option == 's':
      Messages_class.new_message()
      time.sleep(1.5)
      view_friends_general()
      
    if specific_friend_option == 'u':
      personal_dict1 = pickle.load(open("z_folder/z_" + other_functions.f2_var + '.db', 'rb'))
      friend_dict1 = pickle.load(open("z_folder/z_" + choicefriend + '.db', 'rb'))
      if str(input("You sure you want to unfriend " + choicefriend + '?(y/n)')).lower() != 'y':
        print("Ok, you did not unfriend " + choicefriend + ', taking you back...')
        time.sleep(1.5)
        view_friends_general()
      personal_dict1["Posts&Friends"]["Friends"].remove(choicefriend)
      pickle.dump(personal_dict1, open("z_folder/z_" + other_functions.f2_var + '.db', 'wb'))
      
      friend_dict1["Posts&Friends"]["Friends"].remove(other_functions.f2_var)
      pickle.dump(friend_dict1, open("z_folder/z_" + choicefriend + '.db', 'wb'))
      print("You have unfriended " + choicefriend + ', taking you back...')
      time.sleep(2)
      view_friends_general()


def view_suggestions_general():
  other_functions.clear()
  print("OK, here are your friends suggestions: \n")
  time.sleep(1)
  personal_dict = pickle.load(open("z_folder/z_" + other_functions.f2_var + ".db", "rb"))
  friends = personal_dict["Posts&Friends"]["Friends"]
  used = [friend for friend in friends]
  suggestions = []
  
  if len(friends) == 1:
    suggestions = random.sample(other_functions.all_users, 6)
    for i in suggestions:
      if i not in used:
        print(i)
        used.append(i)
        time.sleep(0.4)
    suggestion_option()
  
  if len(friends) != 1:
    limit = 6
    for i in friends:
      if i not in used:
        friend_dict = pickle.load(open("z_folder/z_" + i + ".db", "rb"))
        if len(friend_dict["Posts&Friends"]["Friends"]) > 1 and str(friend_dict["Posts&Friends"]["Friends"][-1]) not in used:
          suggestions.append(str(friend_dict["Posts&Friends"]["Friends"][-1]))
          used.append(str(friend_dict["Posts&Friends"]["Friends"][-1]))
          limit -= 1
    if limit > 0:

      randomsug = random.sample(other_functions.vall_users,limit)
      suggestions = suggestions + randomsug
      for i in suggestions:
        if i != other_functions.f2_var and i not in friends:
          print(i)
      
  suggestion_option()

def suggestion_option():
  choice = str(input('''
  __________________________________________________
  [B]ack      or
  Enter the user ID for more  ''')).lower()

  possibles1 = other_functions.all_users
  possibles1.append('b')
  while choice not in possibles1:
    choice = str(input("Sorry, please enter a Valid option: ")).lower()
  
  if choice == 'b':
    menu_choice()
    


  if choice in other_functions.all_users:
    user_dict = pickle.load(open("z_folder/z_" + choice + ".db", "rb"))
    print("OK, here is the info for user, " + choice)
    print(user_dict["Setting"].get_info())
    jia = str(input("[A]dd Friend or [B]ack: \n")).lower()
    if jia == 'a':
      personal_dict = pickle.load(open("z_folder/z_" + other_functions.f2_var + ".db", "rb"))
      personal_dict["Posts&Friends"]["Friends"].append(choice)
      pickle.dump(personal_dict, open("z_folder/z_" + other_functions.f2_var + ".db", "wb"))
      dui = pickle.load(open("z_folder/z_" +  choice + ".db", "rb"))
      dui["Posts&Friends"]["Friends"].append(other_functions.f2_var)
      pickle.dump(dui, open("z_folder/z_" + choice + ".db", "wb"))
      print("Ok, " + choice+ " is your friend now!")
      time.sleep(2.5)
      other_functions.clear()
      post_menu()
  
    else:
      suggestion_option()
  

def view_user():
  pass
  friend_option()

def friend_option():
  pass

    