from py_folder import advanced_functions, forums, log_in, Messages_class, other_functions, Posts_class, Search_engine, Setting, SpyderChat, word_list
from profanity import profanity
import string
import random
import sys
import time
def print_slow(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(0.02)

def input_profanity(str1: str):
  raw_input = str(input(str1))
  if profanity.contains_profanity(raw_input) == True:
    print("Warning: Do Not Enter Inappropriate Content!")
    input_profanity(str1)

  return raw_input



def editDistDP(str1, str2, m, n):
    str1 = str(SpyderChat.remove1(str1)).lower()
    str2 = str(SpyderChat.remove1(str2)).lower()

    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                dp[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

                # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace

    return dp[m][n]

res1 = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = random.choice([x for x in range(100)]))) 

res2 = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = random.choice([x for x in range(100)]))) 


import sqlite3
import random
conn = sqlite3.connect("all_english_words.db")
c = conn.cursor()

def generate_string(length):
  import pickle
  all_random_words = pickle.load(open("all_english.db", "rb"))
  result = ''
  while len(random.choice(all_random_words)) != length:
    result = random.choice(all_random_words)
  return result
  

def generate_sentence(length):
  if length == 0:
    random_limit = random.randint(0,40)
    result_list = []
    for i in range(random_limit):
      result_list.append(generate_string(0))
    return str(' '.join(str(x) for x in result_list))
  limit = length
  for i in range(limit):
      result_list.append(generate_string(0))
  return str(' '.join(str(x) for x in result_list))

'''
if length == 0:
    c.execute("""
    SELECT word_itself FROM all_english_words order by random() LIMIT 1
    """)
    for i in c.fetchone():
      return str(i)

  c.execute("""
  SELECT word_itself FROM all_english_words where length(word_itself) = ? order by random() LIMIT 1
  """, (int(length),))
  for i in c.fetchone():
    return str(i)'''