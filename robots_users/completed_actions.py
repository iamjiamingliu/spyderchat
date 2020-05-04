from robots_users.interactions import like_post, send_robot_mail, post_robot_post, add_robot_friend, comment_post, robot_error, reply_robot_mail

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

#iniating process
import pickle
import random
import arrow
import time

all_users = pickle.load(open("central_db_folder/AV.txt", "rb"))

all_user_names = list(all_users.keys())

all_random_sentences = pickle.load(open("random_sentences.db", "rb"))

all_english_words = pickle.load(open("all_english.db", "rb"))

today = str(arrow.now().format('YYYY-MM-DD'))

robot_frequency_list = pickle.load(open("robots_users/robot_active_frequency.db", "rb"))

all_possible_interactions = ['send_mail','send_mail','send_mail', 'new_post', 'send_mail','send_mail','send_mail', 'new_post', 'send_mail', 'new_post', 'send_mail', 'new_post', 'add_friend', 'add_friend', 'add_friend','add_friend', 'add_friend','add_friend', 'add_friend', 'upvote_post', 'upvote_post', 'comment_post''upvote_post',  'upvote_post', 'comment_post''upvote_post', 'upvote_post', 'comment_post']


def robot_randomly_interact_indivisually(current_user: str):
  #loading things
  robot_personal_dict = pickle.load(open("z_folder/z_" + current_user + ".db", "rb"))

  indivisual_interaction_history = []
  indivisual_interaction_history.append("Here is User, " + current_user + ' Robot Activity History on ' + today + ': ')

  interaction_counts = random.randint(1, 5)

  # start interacting
  for i in range(interaction_counts):
    interaction_choice = random.choice(all_possible_interactions)
    
    if interaction_choice == 'send_mail':
      indivisual_interaction_history.append(send_robot_mail(current_user))
    
    elif interaction_choice == 'new_post':
      indivisual_interaction_history.append(post_robot_post(current_user))

    elif interaction_choice == 'add_friend':
      indivisual_interaction_history.append(add_robot_friend(current_user))

    elif interaction_choice == 'upvote_post':
      try:
        indivisual_interaction_history.append(like_post(current_user))
      except:
        print("Process error place: liked_post")
        robot_error(current_user)
        indivisual_interaction_history.append("Error occured in liked post")

    elif interaction_choice == 'comment_post':
      try:
        indivisual_interaction_history.append(comment_post(current_user))
      except:
        print("Process error place: comment_post")
        robot_error(current_user)
        indivisual_interaction_history.append("Error occured in comment_post")


  print("All done for user " + current_user)
  return indivisual_interaction_history



def final_robots_actioning(times):
  initial_time = time.time()
  ps = time.time()
  participants = []
  for i in range(times):
    try:
      start = time.time()
      current_user = random.choice(robot_frequency_list)
      participants.append(current_user)
      add_history(current_user, robot_randomly_interact_indivisually(current_user))
      end = time.time()
      run_time = float(end - start)
      add_statistics(current_user, run_time)
      print("User " + current_user + ' has finished in time ' + str(run_time) + ' seconds. Moving on to the next one...')
      time.sleep(0.2)
    
    except:
      try:
        start = time.time()
        current_user = random.choice(robot_frequency_list)
        participants.append(current_user)
        add_history(current_user, robot_randomly_interact_indivisually(current_user))
        end = time.time()
        run_time = float(end - start)
        add_statistics(current_user, run_time)
        print("User " + current_user + ' has finished in time ' + str(run_time) + ' seconds. Moving on to the next one...')
        time.sleep(0.2)
      except:
        print("There is an error...")
        time.sleep(2.5)

  print("All finished! ")
  print("Statistics: ")
  as1 = time.time()
  print(str(len(list(set(participants)))) + ' robots participated in ' + str(times) + ' time')
  print("Time: " + str(as1 - ps))
  final_time = time.time()
  print(final_time - initial_time)






def add_history(robot_username, action_list):
  '''
  import sqlite3
  conn = sqlite3.connect("robot_history.db")
  c = conn.cursor()
  for i in action_list:
    command = "INSERT INTO robot_history (robot,time,action, action_target) VALUES(?, ?, ?, ?)"
    c.execute(command, (robot_username, today + str(current_time), i, "target hasn't established yet..."))
    conn.commit()
  conn.close()
  '''

def add_statistics(robot_username, time):
  '''
  import sqlite3
  conn = sqlite3.connect("robot_history.db")
  c = conn.cursor()
  c.execute("""INSERT INTO robot_statistics (robot_name, run_time) VALUES (?,?)""", (robot_username, time))
  conn.commit()
  conn.close()
  '''