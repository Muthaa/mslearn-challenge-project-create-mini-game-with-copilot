# write 'Hello world' to the console when the app is run in the terminal or command prompt 
#comment the hello world print statement and run the app again
# print('Hello world')
#lets write the logic for  rock paper scissors game
# import random module
import random
# create a list of the game options
options = ['rock', 'paper', 'scissors']
# create a function that will take the user input and the computer input and determine the winner
#lets validate the user input
def validate_input(user_input):
    if user_input not in options:
        return 'Invalid input. Please enter rock, paper or scissors'
    return True

def determine_winner(user_input, computer_input):
    if user_input == computer_input:
        return 'It\'s a tie'
    elif user_input == 'rock' and computer_input == 'scissors':
        return 'You win'
    elif user_input == 'paper' and computer_input == 'rock':
        return 'You win'
    elif user_input == 'scissors' and computer_input == 'paper':
        return 'You win'
    else:
        return 'You lose'
    
# validate the user input using the validate_input function
def play_game(user_input):
    if validate_input(user_input) != True:
        return validate_input(user_input)
    computer_input = random.choice(options)
    print(f'You chose {user_input}')
    print(f'The computer chose {computer_input}')
    print(determine_winner(user_input, computer_input))

# get the user input    
user_input = input('Enter rock, paper or scissors: ')
#lets add Choose to continue playing. Enter 'yes' to continue or 'no' to stop playing when round ends
play_game(user_input)
continue_playing = input('Choose to continue playing. Enter \'yes\' to continue or \'no\' to stop playing: ')
while continue_playing == 'yes':
     user_input = input('Enter rock, paper or scissors: ') 
     play_game(user_input)
     continue_playing = input('Choose to continue playing. Enter \'yes\' to continue or \'no\' to stop playing: ')
print('Game Over')

# run the app in the terminal or command prompt to play the game
# python app.py
# Enter rock, paper or scissors: rock
# You chose rock
# The computer chose scissors
# You win
# Enter rock, paper or scissors: paper