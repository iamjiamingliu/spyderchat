import names
#(names.get_full_name(gender = 'female'))
from random_username.generate import generate_username
#(generate_username(5))
from py_folder import SpyderChat, advanced_functions
import pickle
import random
import time
import arrow


def create_user(amount):
  all_random_sentences = pickle.load(open("random_sentences.db", "rb"))
  today = arrow.now().format('YYYY-MM-DD')
  current_year = int(today[0 : 4])
  if amount < 4:
    print("There are too little input, so it changed it to 4")
    amount = 4
  all_user_names = generate_username(amount)
  
  for i in all_user_names:
    generated_email = advanced_functions.generate_string(random.randint(2,10)) + '@' + random.choice(['gmail','yahoo','123','360','microsoft',advanced_functions.generate_string(random.randint(3, 5))]) + '.' + random.choice(['com','com','com','org','cn','co','com','com','com','com','com'])

    generated_password = advanced_functions.generate_string(random.randint(5,25))

    generated_hobby = random.choice(all_random_sentences) 
    generated_bio =  random.choice(all_random_sentences)
    generated_phone_number = str(random.randint(1023941849, 12022022022))
    generated_gender = random.choice(['male', 'female'])
    generated_age = random.randint(1,100)

    generated_birthyear = str(current_year - generated_age)
    generated_birth_month = random.randint(1,12)
    if generated_birth_month < 10:
      generated_birth_month = '0' + str(generated_birth_month)
    
    generated_birth_date = random.randint(1,30)
    if generated_birth_date < 10:
      generated_birth_date = '0' + str(generated_birth_date)

    final_birthday = str(generated_birth_month) + '-' + str(generated_birth_date) + '-' + str(generated_birthyear) 

    new_account = SpyderChat.SpyderChatAccount(i.lower(), names.get_full_name(gender = generated_gender), generated_email, generated_phone_number, final_birthday, generated_gender, generated_age, generated_hobby, generated_bio, generated_password.lower())


    a = pickle.load(open("central_db_folder/AV.txt", "rb"))
    a.update({new_account.username: new_account})
    

    pickle.dump(a, open("central_db_folder/AV.txt","wb"))

    new_file_name = 'z_folder/z_' + str(new_account.username) + ".db"

    Personal_messages_dict = {"Inbox":{}, "Sent":{}, "Drafts": {}}

    personal_info_dict = {"Messages": Personal_messages_dict, "Posts&Friends": {"Posts": {}, "Friends": [new_account.username]}, "Chats&Forums": {"Chats": None, "Forums":{"as_owner": {}, "as_participant": {}}},"Setting": new_account}

    pickle.dump(personal_info_dict, open(new_file_name, "wb"))

    x1932 = open("Admin_folder/ZZZZAV.db","wb")

    if len(a.keys()) > 5 :
      pickle.dump(a, x1932)

    x1932.close()

  print("Finished Creating Users!!")