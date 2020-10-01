from random import randint



def game():

    print('Welcome to stone, paper & scissor digital version!!')

    print('Enter: \n1 for stone \n2 for paper \n3 for scissor')

    n = int(input())

    m = randint(1,3)

    print(m)

    if(n == m):

        print("It's a draw.")

    elif(m - n == 1 or m - n == 2):

        print('I won! Yay')

    elif(n - m == 1 or n - m == 2):

        print('You won! Congrats')

    z = input('\n\nDo you want to play again? (y/n)')

    if(z == 'y'):

        print('Another game? You got it boss!')

        game()

    else:

        print('Game Ended!\nHave a nice day :)')

        exit()

game()
