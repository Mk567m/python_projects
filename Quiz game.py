
print("...........................")
import random,os,shutil

while True:
    choices = ['rock','paper','scissors']

    computer_choice = random.choice(choices)

    player_choice = input("Pick one; Rock, paper or scissors: ")

    
    while player_choice not in choices:
        player_choice= input("Pick one; Rock, Paper or Scissor: ").lower()
    
    while player_choice=='':
        player_choice = input("Pick one; Rock, Paper or Scissors: ").lower()

    if player_choice == computer_choice:
        print("-----------------------------------")
        print("Computer picked: "+computer_choice)
        print("-----------------------------------")

        print("============================")
        print("you picked: "+ player_choice)
        print("============================")

        print("**Its a tie! and you won**")

    elif player_choice != computer_choice:
        print("-----------------------------------")
        print("**Computer picked**: "+computer_choice)
        print("-----------------------------------")

        print("============================")
        print("---You picked---: "+player_choice)
        print("============================")
        print("You lose!!!") 
        
        print("************************")
    restart_game = input("Wanna play again (yes or no): ")
    if restart_game != "yes":
            break
input("To leave from here, type exit: ")       


