# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
import social_network_ui
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [Person("Henry", 10)] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def login(self):
        for i in range(len(self.list_of_people)):
            print(i+1,self.list_of_people[i].name)
        loginInput = int(input("Please choose a number:"))
        return(self.list_of_people[loginInput-1])
        

    def create_account(self):
        name = input("Enter username ")
        age = input("Enter age ")
        p1 = Person(name, age)
        self.list_of_people.append(p1)
        pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friendlist = []
        self.blockList = []
        self.messages = []

    def editDetails(self):
        self.name = input("Enter username ")
        self.age = input("Enter age ")

    def add_friend(self, person_object):
        self.friendlist.append(person_object)
        #implement adding friend. Hint add to self.friendlist
        pass

    def block(self, person_object):
        self.blockList.append(person_object)
        pass

    def view_friends(self):
        for i in range(len(self.friendlist)):
            print(i+1, self.friendlist[i].name)
        pass

    def send_message(self, sentFrom, sendTo, message):
        concMessage = (sentFrom.name, message)
        sendTo.messages.append(concMessage)
        pass
    
    def view_messages(self):
        print(self.messages)
        pass