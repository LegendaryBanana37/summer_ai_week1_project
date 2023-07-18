#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    while True:
        choiceMain = social_network_ui.mainMenu()
        currentUser = Person("", 0)
        while True: 
            if choiceMain == "1":
                currentUser = ai_social_network.login()
                manageAccountMenuChoice = social_network_ui.manageAccountMenu()
                while True:
                    if manageAccountMenuChoice == "1":
                        currentUser.editDetails()
                        break
                    elif manageAccountMenuChoice == "2":
                        for i in range(len(ai_social_network.list_of_people)):
                            print(i+1,ai_social_network.list_of_people[i].name)
                        friendInput = int(input("Please choose a number:"))
                        currentUser.add_friend(ai_social_network.list_of_people[friendInput-1])
                        break
                    elif manageAccountMenuChoice == "3":
                        currentUser.view_friends()
                        break
                    elif manageAccountMenuChoice == "4":
                        for i in range(len(ai_social_network.list_of_people)):
                            print(i+1,ai_social_network.list_of_people[i].name)
                        blockInput = int(input("Please choose a number:"))
                        currentUser.block(ai_social_network.list_of_people[blockInput-1])
                        break
                    elif manageAccountMenuChoice == "5":
                        for i in range(len(ai_social_network.list_of_people)):
                            print(i+1,ai_social_network.list_of_people[i].name)
                        messageChoiceInput = int(input("Please choose a number:"))
                        if ai_social_network.list_of_people[messageChoiceInput-1].blockList.__contains__(currentUser):
                            print("YOU HAVE BEEN BLOCKED!")
                            break
                        else:
                            messageInput = input("Enter message")
                            currentUser.send_message(currentUser, ai_social_network.list_of_people[messageChoiceInput-1], messageInput)
                            break
                    elif manageAccountMenuChoice == "6":
                        currentUser.view_messages()
                        break
                    elif manageAccountMenuChoice == "7":
                        break
                    else:
                        manageAccountMenuChoice = social_network_ui.manageAccountMenu()
                break
            elif choiceMain == "2":
                ai_social_network.create_account()
                break

            elif choiceMain == "3":
                print("Thank you for visiting. Goodbye.")
                quit()

            else:
                print("Your input is invalid. Try Again!")
        #restart menu
            break



        
