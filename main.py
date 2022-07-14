import random
from replit import clear
from art import logo,you_win,you_lose
def play_game():
    print(logo)
    
    num=random.randint(1,100)
    life=0

    print("I,m thinking of a number between 1 to 100.")
    user_level=input("Choose a difficulty.Type 'e' for Easy level or Type 'h' for Hard Level = " ).lower()
    
    if user_level=='e':
        life=10
    elif user_level =='h':
        life=5
    else:
        print("Invlid choose")
        
    while life !=0 :            
        print(f"You have {life} attempts remaining to guess the number.")
        user_guess=int(input("Make a guess of number = "))
        if user_guess==num:
            print(you_win)
            print("Your guess is correct ,You win.")
            life=0 
        elif user_guess<num:
            print(f"Too High.\nGuess again.")
            life-=1
        else:
            print("Too Low.\nGuess again")
            life-=1                   

    if life==0 and user_guess!=num:
        print(you_lose)
        print("You've run out of guesses,you lose.")
               
while input("Do you want play a gamee of Guess the Number Type 'y' or 'n' = ")=='y':
    clear()
    play_game()          