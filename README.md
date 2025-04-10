# IFCS1-SUMM1

## User Documentation

### Overview

The `IFCS1-SUMM1` project is a Python-based maths game that requires solving basic linear equations to reach a high score.<br>
This documentation will provide you with the knowledge needed to run this game on your local computer.  

### Prerequisites
Before beginning, please make sure you have installed or install the following software:

•	`Python 3.12.7`


### Prerequisite Installation Instructions
1. Install `Python 3.12.7`

    - Windows: Download Python from [python.org](https://www.python.org/downloads/windows/)
    - macOS: Download Python [python.org](https://www.python.org/downloads/mac-osx/)


Once the download is complete, launch the installer and proceed by following the on-screen prompts.  
During the installation process, ensure you have selected the option labelled "Add Python to PATH."  

This will allow you to run the game in your terminal, but if you need to leave this option unchecked, the game can also run using an IDE such as Visual Studio Code, available at [code.visualstudio.com](https://code.visualstudio.com/)


### Project Installation Instructions
1. Under `code`, press `download zip` and save to a folder of your choosing.
2. Extract the .zip file to a normal folder.

### How to Run the Game
1. Open Terminal (macOS) or Command Prompt (Windows, aka ‘CMD’)
2. In Terminal or CMD, navigate to the folder where you saved the extracted zip project files
3. In Terminal or CMD, type:
```
python3 main.py
```

You should then have the following message appear:
```
✖️ ➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰 ✖️
✖️ Welcome to a linear equations maths game✖️
✖️ ➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰 ✖️

How many questions would you like to solve?:
```

### Playing the Game

The user is prompted to enter how many linear equations they would like to solve, the number entered will determine their overall score.  
The more questions that are answered correctly, the higher the score they can obtain.

After this, the user is then faced with a randomly generated linear algebra equation:
```
Question 1:
4 * 1x = 12

Solve for x. Enter your answer:
```
The user then inputs their answer and is informed if they have answered correctly or incorrectly.

•	If answered correctly, they gain a point.  
•	If answered incorrectly, the correct answer appears.

The next question (if the user requested more than 1 question) then follows:

```

Solve for x. Enter your answer: 3

Correct!


Question 2:
1 * 3x = 6

Solve for x. Enter your answer:
```

Once all the requested questions are answered, either correctly or incorrectly, the user is informed the game is over, the score they got, and an option to play again or quit.

```
Question 3:
1 * 3x = 12

Solve for x. Enter your answer: 3

Incorrect! The correct answer is 4.

Game over. Your score is 2/3.

Would you like to play again? (y/n):
```

If the user enters ‘y’, the game repeats.
If the user enters anything else, the game quits.



## Technical Documentation

### Project Structure
```
IFCS1-SUMM1/
├── main.py           		# Main file for running the game, calls the below functions
├── games.py      		# Runs the game through the function maths_game()
├── questions.py  		# Generates random, answerable linear equations
```

### Project Files
#### main.py
This file launches the linear equation maths game from `games.py` by importing the `maths_game` function.  
It also controls the loop for the game to be played indefinitely depending on the users wish, using the function `loop_maths_game(play_game)` which takes a single parameter `play_game`, and uses this to loop the `launch_maths_game()` function.  

#### Functions
#### Launch_maths_game()
```
def launch_maths_game():
        
        # New lines for readability
        print("") 
        print("") 
        
        # Launch the maths game
        maths_game()
```
This function launches the `maths_game()` function imported from `games.py`.  

#### Loop_maths_game(play_game)
```
def loop_maths_game(play_game):
    while play_game == "y":

        # Launch the maths game
        launch_maths_game()

        # Ask the user if they want to play again
        play_game = input("Would you like to play again? (y/n): ").lower()

```
This function launches the maths game under a loop which, after the first game, asks the user if they want to play again and sets the variable `play_game` accordingly, staying in the loop if the user responds with `y`.  
It is assumed that any input other than `y` is `n`, and the script will end here.  

#### games.py

#### Functions
This file has a single function called `maths_game()` which introduces and plays the game, taking inputs of `total_questions` and `user_answer` and uses error handling with `isinstance` and `try/except` to catch invalid (non-integer) inputs.  

It generates the maths questions and answers using the `generate_linear_equation` function which is imported from `questions.py` and then equates these with `user_answer` to increment `user_score` and `question_number` to track the overall score which is displayed at the end in the form of `user_score/total_questions`.

#### questions.py

#### Functions
This file has a single function called `generate_linear_equation()` which generates a linear equation in the form `a + bx = y`.  

```
def generate_linear_equation():

    # Generate random values for alpha, beta, and gamma
    alpha = random.randint(1, 10)
    beta = random.randint(1, 10)
    gamma = random.randint(2, 20)

    # Calculate the answer to the equation
    correct_answer = (gamma / alpha) / beta

    # Check if the answer is an integer. If not, generate new values for alpha, beta, and gamma.
    while correct_answer % 1 != 0:
        alpha = random.randint(1, 10)
        beta = random.randint(1, 10)
        gamma = random.randint(2, 20)
        correct_answer = (gamma / alpha) / beta

    # Convert the answer to an integer
    linear_eq_answer = int(correct_answer)

    return alpha, beta, gamma, linear_eq_answer
```

It generates random values using the imported `random` module, and checks that the answer to the question is a positive integer, and if not, it generates new values until it finds a desirable solution. The user should not need a calculator to play the game.  

The function returns `a`, `b` and `y` values, as well as the answer to the question (`x`), and refers to these with the variables `alpha`, `beta`, `gamma`, and `linear_eq_answer` respectively.

### Dependencies
•	The files use Python’s built-in libraries `random`, `input()` and `isinstance()`.  
•	No external installations or packages are needed.
