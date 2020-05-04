#iniating process
import pickle
import random
import time
import arrow
from py_folder import Messages_class, Posts_class

make_sense_replies = ['Got it', 'I see','Well, I do not know what to even say about this...', 'Hey Friend, I just got your message. Unfortunately, it is a little bit sensitive to ask, so I guess that is out of my ability.', 'I can try...','sorry, i apologize that I cannot say anything about this mail.','?','hold on can you repeat your mail please?', 'sorry i do not understand...','please do not send me random messages.']


all_users = pickle.load(open("central_db_folder/AV.txt", "rb"))

all_user_names = list(all_users.keys())

all_random_sentences = pickle.load(open("random_sentences.db", "rb"))

all_english_words = pickle.load(open("all_english.db", "rb"))

today = str(arrow.now().format('YYYY-MM-DD'))

robot_frequency_list = pickle.load(open("robots_users/robot_active_frequency.db", "rb"))

all_possible_interactions = ['send_mail','send_mail','send_mail', 'new_post', 'send_mail','send_mail','send_mail', 'new_post', 'send_mail', 'new_post', 'send_mail', 'new_post', 'add_friend', 'add_friend', 'add_friend','add_friend', 'add_friend','add_friend', 'add_friend', 'upvote_post', 'upvote_post', 'comment_post''upvote_post',  'upvote_post', 'comment_post''upvote_post', 'upvote_post', 'comment_post']

# here are the functions

def robot_error(current_user: str):
  print("An error has occured with robot " + current_user)
  #a = input("Enter CONTINUE to continue, otherwise automatically exit: ")
  #if a != 'CONTINUE':
    #exit()
  time.sleep(1)


def add_robot_friend(current_user: str):
  # find random possibles
  robot_personal_dict = pickle.load(open("z_folder/z_" + current_user + ".db", "rb"))

  friends = robot_personal_dict["Posts&Friends"]["Friends"]
  
  used = [friend for friend in friends]
  suggestions = []
  
  suggestions = random.sample(all_user_names, 6)
  for i in suggestions:
    if i in used:
      suggestions.remove(i)
      new_suggestion = random.choice(all_user_names)
      suggestions.append(new_suggestion)
      used.append(new_suggestion)

  # select one and add friend randomly (the next one is just to make sure)
  for i in suggestions:
    if i in friends:
      suggestions.remove(i)
  
  if len(suggestions) == 0:
    print("There is no one to suggest!")
    robot_error(current_user)
  
  new_robot_friend = str(random.choice(suggestions))
  new_robot_friend_dict = pickle.load(open("z_folder/z_" + new_robot_friend + ".db", "rb"))
  
  robot_personal_dict["Posts&Friends"]["Friends"].append(new_robot_friend)

  pickle.dump(robot_personal_dict, open("z_folder/z_" + current_user + ".db", "wb"))

  new_robot_friend_dict["Posts&Friends"]["Friends"].append(current_user)

  pickle.dump(new_robot_friend_dict, open("z_folder/z_" + new_robot_friend + ".db", "wb"))

  print(current_user + ' has added friend with '+ new_robot_friend)

  return str(current_user + ' has added friend with '+ new_robot_friend)
  
  
def send_robot_mail(current_user: str):
  #loading things
  robot_personal_dict = pickle.load(open("z_folder/z_" + current_user + ".db", "rb"))
  BiggestID = pickle.load(open("central_db_folder/BiggestID.txt", "rb"))
  BiggestID += 2
  # creating class object
  robot_mail_content = random.choice(all_random_sentences)
  robot_mail_receivers = random.choices(robot_personal_dict["Posts&Friends"]["Friends"])
  robot_mail_subject = random.choice(all_english_words)

  new_mail_object = Messages_class.Messages(current_user, robot_mail_receivers, robot_mail_subject, robot_mail_content, today, None, BiggestID, {})

  # send the object and update id
  
  for receiver in new_mail_object.receivers:
      receiver_file_name = 'z_folder/z_' + receiver + ".db"
      receiver_info = pickle.load(open(receiver_file_name, "rb"))
      receiver_info["Messages"]["Inbox"].update({int(new_mail_object.ID): new_mail_object})
      pickle.dump(receiver_info, open(receiver_file_name, "wb"))

  robot_personal_dict["Messages"]["Sent"].update({int(new_mail_object.ID): new_mail_object})
  pickle.dump(robot_personal_dict, open("z_folder/z_" + current_user + ".db", "wb"))

  # notify the admin
  print(current_user + ' has sent a mail to ' + str(len(new_mail_object.receivers)) + ' receivers')
  return str(current_user + ' has sent a mail to ' + str(len(new_mail_object.receivers)) + ' receivers')

def post_robot_post(current_user: str):
  #loading things
  robot_personal_dict = pickle.load(open("z_folder/z_" + current_user + ".db", "rb"))
  BiggestID = pickle.load(open("central_db_folder/BiggestID.txt", "rb"))
  BiggestID += 1
  #create_object
  robot_post_content = random.choice(all_random_sentences)

  robot_post_object = Posts_class.Posts(current_user, robot_post_content, today, random.randint(1, len(robot_personal_dict["Posts&Friends"]["Friends"])), random.choices(all_random_sentences), BiggestID, robot_personal_dict["Posts&Friends"]["Friends"])

  # pickle job
  for friend in robot_post_object.viewers:
    friend_file = "z_folder/z_" + friend + ".db"
    friends_dict = pickle.load(open(friend_file, "rb"))
    friends_dict["Posts&Friends"]["Posts"].update({BiggestID: robot_post_object})
    pickle.dump(friends_dict, open(friend_file, "wb"))

  pickle.dump(BiggestID + 1, open("central_db_folder/BiggestID.txt", "wb"))

  print(current_user + ' has succesfully posted a new post!')
  return str(current_user + ' has succesfully posted a new post!')


def comment_post(current_user: str):
  #loading things
  robot_personal_dict = pickle.load(open("z_folder/z_" + current_user + ".db", "rb"))
  
  #start adding
  post_choice = int(random.choice(list(robot_personal_dict["Posts&Friends"]["Posts"].keys())))
  input_comment = random.choice(all_random_sentences)

  viewers1 = robot_personal_dict["Posts&Friends"]["Posts"][int(post_choice)].viewers  
  
  for viewer in viewers1:
    view_dict = pickle.load(open("z_folder/z_" + viewer + ".db", "rb"))
    view_dict["Posts&Friends"]["Posts"][int(post_choice)].comments.append(input_comment)
    pickle.dump(view_dict, open("z_folder/z_" + viewer + ".db", "wb"))

  print(current_user + " has success commented in one of the post!" )

  return str(current_user + " has success commented in one of the post!" )

def like_post(current_user: str):
  #loading things
  robot_personal_dict = pickle.load(open("z_folder/z_" + current_user + ".db", "rb"))
  post_choice = int(random.choice(list(robot_personal_dict["Posts&Friends"]["Posts"].keys())))
  viewers1 = robot_personal_dict["Posts&Friends"]["Posts"][int(post_choice)].viewers
  for viewer in viewers1:
    view_dict = pickle.load(open("z_folder/z_" + viewer + ".db", "rb"))
    view_dict["Posts&Friends"]["Posts"][int(post_choice)].up_votes += 1
    pickle.dump(view_dict, open("z_folder/z_" + viewer+ ".db", "wb"))

  print(current_user + " has success liked in one of the post!" )

  return str(current_user + " has success liked in one of the post!" )



def reply_robot_mail(current_user: str, replyID: int, receiver: str):
  final_receivers = []
  final_receivers.append(receiver)

  taken_ID = int(pickle.load(open("central_db_folder/BiggestID.txt","rb")))

  ID1 = taken_ID + 2

  receiver_file_name = 'z_folder/z_' + str(receiver) + ".db"
  
  receiver_info = pickle.load(open(receiver_file_name, "rb"))
  
  
      
  pickle.dump(receiver_info, open(receiver_file_name, "wb"))
  
  subject1 = str('Reply to Your Message with ID ' + str(replyID) + '')

  content1 = random.choice(make_sense_replies)

  pickle.dump(ID1, open("central_db_folder/BiggestID.txt","wb"))


  new_message_class_object = Messages_class.Messages(current_user, final_receivers, subject1, content1, today, None, ID1, [])


  try:
    receiver_info["Messages"]["Inbox"][replyID].reply.update({ID1: new_message_class_object})

  except:
    pass

  try:
    receiver_info["Messages"]["Sent"][replyID].reply.update({ID1: new_message_class_object})
    
  except:
    pass
  
  new_message_class_object.send_message(new_message_class_object)

  wi102 = open('z_folder/z_' + current_user + '.db', "rb")

  sent_dict = pickle.load(wi102)

  sent_dict["Messages"]["Sent"].update({new_message_class_object.ID: new_message_class_object})

  pickle.dump(sent_dict, open('z_folder/z_' + current_user + '.db', "wb"))

  wi102.close()

  print(current_user + ' has replied to a message with ID, ' + replyID)

  return str(current_user + ' has replied to a message with ID, ' + replyID)

