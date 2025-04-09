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
