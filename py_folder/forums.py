from py_folder import advanced_functions, forums, log_in, Messages_class, other_functions, Posts_class, Search_engine, Setting, SpyderChat, word_list

from termcolor import colored
import pickle
import arrow
import time


class forum():
    def __init__(self, forum_name, forum_description, forum_participants,
                 forum_owner, forum_answers, forum_category, forum_question,
                 public, password, date):
        self.forum_name = forum_name
        self.forum_description = forum_description
        self.forum_participants = forum_participants
        self.forum_owner = forum_owner
        self.forum_answers = forum_answers
        self.forum_category = forum_category
        self.forum_question = forum_question
        self.public = public
        self.password = password
        self.date = date

    def view_forum(self):
        print("This function will be ready in Spyderchat version 0.06!")
        time.sleep(2)

    def is_public(self):
        return self.public == True

    def is_private(self):
        return self.public == False

    class question():
        def __init__(self, heckler, date, upvotes, comments, content):
            self.heckler = heckler
            self.date = date
            self.upvotes = upvotes
            self.comments = comments
            self.content = content

    class answers():
        def __init__(self, responder, date, upvotes, comments, content):
            self.responder = responder
            self.date = date
            self.upvotes = upvotes
            self.comments = comments
            self.content = content

    class comments():
        def __init__(self, commenter, date, upvotes, comments, content):
            self.commenter = commenter
            self.date = date
            self.upvotes = upvotes
            self.comments = comments
            self.content = content


def entered_option():
    personal_file_name = 'z_folder/z_' + other_functions.f2_var + '.db'
    personal_dict = pickle.load(open(personal_file_name, "rb"))
    personal_dict_forum_section = personal_dict["Chats&Forums"]["Forums"]
    other_functions.clear()
    print(
        colored(
            "Welcome to the newest feature of SpyderChat, Forums!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
            "red"))
    time.sleep(2)

    if len(personal_dict_forum_section["as_owner"].keys()) > 0 or len(
            personal_dict_forum_section["as_participant"].keys()) > 0:
        print(colored('Here are the existing Forums you have:', "red"))
        time.sleep(1)
        print('''
+----------------------------------------+
Forum Name (you are the owner)''')
        time.sleep(0.5)
        for key, item in personal_dict_forum_section["as_owner"].items():
            general_view = '| ' + item.forum_name + '    ' + '    created at ' + item.date + ' |'
            print(colored(general_view, "red"))
            time.sleep(0.5)

        print('''
+----------------------------------------+
Forum Name (you are NOT the owner)''')
        time.sleep(0.5)
        for key, item in personal_dict_forum_section["as_participant"].items():
            general_view = '|' + item.forum_name + '    ' + item.forum_owner + '    created at ' + item.date + '|'
            print(colored(general_view, "red"))
            time.sleep(0.5)
        print("+----------------------------------------+")
    else:
        print(
            "You have no Forum Yet! Why not try to Join one or create your own!"
        )
    entered_choice()


def entered_choice():
    personal_file_name = 'z_folder/z_' + other_functions.f2_var + '.db'
    personal_dict = pickle.load(open(personal_file_name, "rb"))

    entered_choice1 = str(
        input('''
  +----------------------------------------+
  Enter a Forum Name to View Specifically, or
  [N]ew Forum       [B]ack           [H]elp   
  '''))

    if entered_choice1.lower() == 'b':
        log_in.second_option()

    if entered_choice1.lower() == 'h':
        print(log_in.User_manual)
        time.sleep(7)
        entered_choice()

    if entered_choice1.lower() == 'n':
        object_forum = new_forum()
        a321 = str(
            input(
                "Would you like to invite your friends into this forum? [Y/N]")
        ).lower()

        if a321 == 'y':
            invitation_content = '''
      Hello, Friend!
      
        I just started a new Forum. Here is a description for it:
      ''' + "\n" + object_forum.forum_description + '''
      I really hope you can join this forum. Why not go search ''' + object_forum.forum_name + " on SpyderChat, and you then can join!"

            taken_ID = int(pickle.load(open("central_db_folder/BiggestID.txt", "rb")))
            ID1 = taken_ID + 2

            pickle.dump(ID1, open("central_db_folder/BiggestID.txt", "wb"))

            new_message_class_object = Messages_class.Messages(
                other_functions.f2_var,
                personal_dict["Posts&Friends"]["Friends"],
                "Your Friend " + other_functions.f2_var +
                " is inviting you to a forum!", invitation_content,
                str(arrow.now().format('YYYY-MM-DD')), None, ID1, [])

            Messages_class.Messages.send_message(new_message_class_object)

            print(colored('Success!', "red"))
            time.sleep(2)
            entered_option()

    cur_all_forums = personal_dict["Chats&Forums"]["Forums"]["as_owner"]
    cur_all_forums.update(
        personal_dict["Chats&Forums"]["Forums"]["as_participant"])

    while entered_choice1 not in list(cur_all_forums.keys()):
        print("\n Sorry, please enter a valid option")
        entered_choice()
    wgfdsiosj = 'Need to complete here!'


def new_forum():
    print(
        colored(
            "OK, you are creating a new forum, please follow the instructions carefully.",
            "red"))
    time.sleep(2)
    other_functions.clear()
    input_name = str(
        input('''
    +-----------------------------------------+
    | Enter this forum's name:                |
    +-----------------------------------------+
    ''')).lower()

    input_description = str(
        input('''
    +-----------------------------------------+
    | Please give a description:              |
    +-----------------------------------------+
    ''')).lower()

    input_question = str(
        input('''
    +-----------------------------------------+
    | Please enter the content                |
    | (only one paragraph without new lines)  |
    +-----------------------------------------+
    '''))

    input_public = str(
        input('''
    +-----------------------------------------+
    | Do you want it to be a public forum?    |
    | [Y]es     [N]o                          |
    +-----------------------------------------+
    ''')).lower()

    while input_public not in ['y', 'n']:
        input_public = str(input("only enter Y or N: ")).lower()

    if input_public == 'y':
        input_public = True
        input_password = ''

    else:
        input_public = False
        input_password = str(
            input('''
    +----------------------------------------+
    | Please set a password for your forum:  |
    +----------------------------------------+
      ''')).lower()

    input_category = str(
        input('''
    +------------------------------------------+
    | Tell us the category for the forum       |
    |       (In no more than two words!)       |
    +------------------------------------------+
    ''')).lower()

    while len(input_category) >= 30:
        input_category = str(
            input('''
      +------------------------------------------+
      | Sorry, try to enter a shorter one!       |
      | Tell us the category for the forum       |
      |       (In no more than two words!)       |
      +------------------------------------------+
    ''')).lower()

    new_forum_object = forum(input_name, input_description, [],
                             other_functions.f2_var, {}, input_category,
                             input_question, input_public, input_password,
                             str(arrow.now().format('YYYY-MM-DD')))

    if new_forum_object.is_public() == True:
        is_public_string = 'public'
    else:
        is_public_string = 'private'

    cur_all_forums = pickle.load(open("central_db_folder/all_forums.db", "rb"))
    cur_all_forums[is_public_string].update({
        new_forum_object.forum_name:
        new_forum_object
    })
    pickle.dump(cur_all_forums, open("central_db_folder/all_forums.db", "wb"))

    personal_dict = pickle.load(
        open("z_folder/z_" + other_functions.f2_var + ".db", "rb"))
    personal_dict["Chats&Forums"]["Forums"]["as_owner"].update({
        new_forum_object.forum_name:
        new_forum_object
    })
    pickle.dump(personal_dict, open("z_folder/z_" + other_functions.f2_var + ".db",
                                    "wb"))

    print("You have succesfully created forum, " +
          new_forum_object.forum_name + "!")
    time.sleep(2)
    return new_forum_object
