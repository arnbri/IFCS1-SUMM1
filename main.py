# Import the maths_game function from the games module
from games import maths_game 

'''
This module launches the maths game
'''

# Function to launch the maths game
def launch_maths_game():
        
        # New lines for readability
        print("") 
        print("") 
        
        # Launch the maths game
        maths_game()

# Function to loop the maths game
def loop_maths_game(play_game):
    while play_game == "y":

        # Launch the maths game
        launch_maths_game()

        # Ask the user if they want to play again
        play_game = input("Would you like to play again? (y/n): ").lower()


loop_maths_game("y")