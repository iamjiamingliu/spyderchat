'''

''
#再见！现在我们需要创造一个function去创造一大堆accounts因为更新把老的accounts都废了。and, we need ot start uding sqlite to store out data- because that is the fastest we we can trtreive the data. 加油！also, try to create a sentene generator that generates sentence LOGICALLy

from py_folder import other_functions, SpyderChat

import os
import pickle
from termcolor import colored
import sys
import time


# Here are the initating process:

# this is profanity check loading

#this is print slow function
def print_slow(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.05)


#this is greeting

cur_version = '''SpyderChat Version: 0.05
New Features: Fully Functioning Post&Friends Section and Colors
Ready User?
'''

print_slow(colored(cur_version, "green"))

time.sleep(4)
file_path = "central_db_folder/AV.txt"

#this is loading files from dbs
cur1 = {}
if os.stat(file_path).st_size != 0:
  cur1 = pickle.load(open(file_path,"rb"))
  other_functions.Accountdb = cur1



other_functions.Accountdb = cur1
SpyderChat.accounts_dictionary = cur1
other_functions.f1_var = cur1


other_functions.all_users = [x for x in other_functions.f1_var.keys()]


other_functions.vall_users = other_functions.all_users
try: 
  other_functions.vall_users.remove("b")

  other_functions.vall_users.remove("fns")

except:
  pass


#finally!
SpyderChat.greeting()
other_functions.f2_var = username = other_functions.first_option()


exit()

