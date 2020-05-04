# Here are the admin functions:
'''
word_list.send_admin_message()
exit()
'''
'''
new_account = SpyderChat.SpyderChatAccount('alexfang', 'james charles', 'james@gmail.com', '2022022022', '01-01-2001', 'na', 20, 'bobby is none',
                                    'hi sisters!', '12345')                 
all1 = pickle.load(open("central_db_folder/AV.txt", 'rb'))
all1.update({new_account.username: new_account})
pickle.dump(all1, open("central_db_folder/AV.txt", "wb"))

new_file_name = 'z_' + str(new_account.username) + ".db"

Personal_messages_dict = {"Inbox":{}, "Sent":{}, "Drafts": {}}

personal_info_dict = {"Messages": Personal_messages_dict, "Posts&Friends": {"Posts": {}, "Friends": [new_account.username]}, "Chats&Forums": None,"Setting": new_account}

pickle.dump(personal_info_dict, open(new_file_name, "wb"))


exit()
'''

'''for i in other_functions.all_users:
  print_slow(i)
  file_name = 'z_' + str(i) + '.db'
  file_dict = pickle.load(open(file_name, "rb"))
  pickle.dump(file_dict, open(file_name, "wb"))
  print_slow(i + 'is finished')
  time.sleep(0.5)'''
  
#other_functions.f2_var == 'admin2'

#Messages_class.reply_message(1025, "admin1")

'''
av = pickle.load(open("central_db_folder/AV.txt", "rb"))
all_users = list(av.keys())
for user in all_users:
  try:
    

  except:
    print_slow("There is error in user " + user + '!')
    time.sleep(4)
'''
'''
import os
import sqlite3
conn = sqlite3.connect("central_db_folder/all_users")
c = conn.cursor()
c.execute("""
create table central_users_info (
  username text,
  user_class_object 
)
""")
dirs = os.scandir('z_folder')
for i in dirs:
  print(i.name)

exit()
'''
'''
import os
import pickle
version1_dict = {"All_Users_Specifically":{}}



dirs = os.scandir('z_folder')
for i in dirs:
  try:
    user_dict = pickle.load(open('z_folder/' + i.name, "rb"))
    version1_dict["All_Users_Specifically"].update({user_dict["Setting"].username: user_dict})
  except:
    print(i.name + ' is outdated')

pickle.dump(version1_dict, open("central_db_folder/all_users", "wb"))

afterall = pickle.load(open("central_db_folder/all_users", "rb"))
print(afterall)

exit()
'''

'''
import pickle
a = pickle.load(open("central_db_folder/all_users", "rb"))
for i in a["All_Users_Specifically"].keys():
  print(i)
exit()
'''
'''
import time
start = time.time()

import sqlite3
conn = sqlite3.connect("all_english_words.db")
c = conn.cursor()
c.execute("""
  SELECT word_itself FROM all_english_words WHERE LENgth(word_itself) = 5 order by random() LIMIT 1
""")
for i in c.fetchone():
  print(str(i))
end = time.time()
print("The program is complete and compiled in ", end-start, "seconds.")
exit()
'''


'''
for i in range(1000):
  import pickle
  file1 = open("all_generated_sentences.db", "rb")
  cur_sentences_list = pickle.load(file1)

  import time
  start = time.time()
  from py_folder import advanced_functions

  for i in range(5):
    cur_generation = advanced_functions.generate_sentence(0)
    cur_sentences_list.append(cur_generation)

  file1 = open("all_generated_sentences.db", "wb")

  pickle.dump(cur_sentences_list, file1)
  end = time.time()
  
  print("The sub program is complete and compiled in ", end-start, "seconds.")
  print(len(cur_sentences_list))
'''


'''
# here are the funcitons used to create random sentences
import pickle
import time
a = pickle.load(open("random_sentences.db", "rb"))
print(len(a))
for i in a:
  print(i)
  time.sleep(1)
exit()

def create_sentences(times):
  final_new_sentences = []
  import random
  import pickle
  import time

  existing_all_sentences = pickle.load(open("random_sentences.db", "rb"))

  initial_starting = time.time()

  print("Ok, you will get approximately create, \n %d new random sentences in random_sentences.db." %(times))
  time.sleep(2)
  print("\n\n")
  #loading words
  a = pickle.load(open("test_words.db", "rb"))
  print("Things are all set, start creating...")
  print('\n\n')
  
  initial_100000 = time.time()

  for i in range(times):
    #tell progress

    if i % 100000 == 0 and i > 1:
      finished_100000 = time.time()
      print("There are %d sentences now, \n %d to go, keep creating... " %(len(final_new_sentences), times - len(final_new_sentences)))
      print("It took %d seconds to create these..." %(finished_100000 - initial_100000))
      initial_100000 = time.time()
      
      if len(final_new_sentences) >= 100000:
        existing_all_sentences = existing_all_sentences + final_new_sentences
        
        pickle.dump(existing_all_sentences, open("random_sentences.db", "wb"))
        existing_all_sentences = []
        print("Your random_sentences.db is updated, keep going...")
        print(str(len(existing_all_sentences)) + ' sentences in existing file')
        print(str(len(final_new_sentences)) + ' created')
        print("\n\n\n")

    count = random.randint(5, 35)
    all_random_words = random.choices(a, k = count)
    
    #turning list of words into string of a sentence then append
    final_new_sentences.append(str(' '.join(x.rstrip() for x in all_random_words)))
  if len(final_new_sentences) >= times - 1:
    pickle.dump(final_new_sentences, open("random_sentences.db", "wb"))
  final_completion = time.time()
  print("Congradulation! There are %d new sentences created for you!" %(len(final_new_sentences)))
  print("It took %d seconds to get all of these done!" %(final_completion - initial_starting))
  time.sleep(5)
  for i in final_new_sentences:
    print(i)
    time.sleep(2)
  print(final_new_sentences)



create_sentences(11000)
exit()

'''

'''a_file = open("test1.txt", "r")
import random
list_of_lists = []
for line in a_file:
  stripped_line = line
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

a_file.close()

final_list = []
for i in list_of_lists:
  for w in i:
    choice = random.choice([1,2,3,4,5])
    if choice == 1:
      final_list.append(w)
import pickle
pickle.dump(final_list, open("all_english.db", "wb"))
print(len(final_list))
exit()
'''

'''

from robots_users import create_robot
create_robot.create_user(5)
exit()
'''
'''

import pickle
cur = pickle.load(open("central_db_folder/AV.txt", "rb"))
new_cur = []
for key, item in cur.items():
  new_cur.append(key)
len1  = len(new_cur)

import random
for i in new_cur:
  if random.choice([1,2,3,4]) == 1:
    new_cur.append(i)
    new_cur.append(i)
    new_cur.append(i)
if random.choice([1,2,3,4]) == 2:
    new_cur.append(i)
    new_cur.append(i)
if random.choice([1,2,3,4]) == 3:
    new_cur.append(i)
print(len1)
print(len(new_cur))

pickle.dump(new_cur, open("robots_users/robot_active_frequency.db", "wb"))

print(new_cur)
exit()
'''