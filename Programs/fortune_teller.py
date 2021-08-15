import random

print("Welcome to your fortune teller! Feel free to ask any question. Remember, no inappropriate questions!")
while(True):
    choice = str(input("Do you wish to continue? (Y\y or N/n): "))
    if(choice.lower() == 'y'):
        question = input("Ask a question: ")
        n = random.randint(0,8)
        if(n==0):
            print("Yes\n")
        elif(n==1):
            print("Ask me later\n")
        elif(n==2):
            print("Better to go with a 'no'...\n")
        elif(n==3):
            print("Certainly for sure!\n")
        elif(n==4):
            print("You might not want to know now...\n")
        elif(n==5):
            print("Probably not\n")
        elif(n==6):
            print("Never\n")
        elif(n==7):
            print("There are high chances!\n")
        elif(n==8):
            print("You may conclude so.\n")
        else:
            break

    elif(choice.lower() == 'n'):
        print("Thank you for playing. Come back soon!\n")

    else:
        print("Please enter a valid option!\n")

    
    
