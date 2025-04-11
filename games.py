# Import the function to generate linear equations from the questions module
from questions import generate_linear_equation 

def maths_game():
    '''
    A maths game that generates linear equations and asks the user to solve them.
    The game prompts the user to specify the number of questions they want to solve.
    For each question, it generates a linear equation in the form alpha + (beta)x = gamma,
    and asks the user to solve for x. The user's score is displayed at the end.

    Returns:
    None

    Raises:
    ValueError: If the user input for the number of questions is not a positive integer.
    ValueError: If the user input for the answer is not a positive integer.
    '''
    # Introduce the game
    print("✖️ ➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰 ✖️")
    print("✖️ Welcome to a linear equations maths game✖️")
    print("✖️ ➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰✖️➕➖➗🟰 ✖️")
    print("")
    
    # Ask the user for the number of questions
    total_questions = input("How many questions would you like to solve?: ") 

    # Check if the input is a positive integer, if not, ask again
    while not isinstance(total_questions, int): 
        try:
            total_questions = int(total_questions)
            if total_questions <= 0:
                raise ValueError("Number of questions must be positive.")
        except ValueError:
            total_questions = input("Please enter a valid number of questions: ")

    # Ask the user as many linear equation questions as requested
    question_number = 0
    user_score = 0
    
    for _ in range(total_questions):
        # Generate a linear equation and extract the values
        alpha, beta, gamma, correct_answer = generate_linear_equation()
        question_number += 1
        print("")
        print(f"Question {question_number}:")
        print(f"{alpha} * {beta}x = {gamma}")
        print("")
        user_answer = input("Solve for x. Enter your answer: ")

        # Check if the input is a positive integer, if not, ask again
        while not isinstance(user_answer, int):
            try:
                user_answer = int(user_answer)
                if user_answer <= 0:
                    raise ValueError("Answer must be positive.")
            except ValueError:
                user_answer = input("Please enter a valid answer (must be a number): ")
        
        # New line for readability
        print("") 

        # Check if the user answer is correct, if not, provide the correct answer
        if user_answer == correct_answer:
            print("Correct!")
            user_score += 1
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")
        
        # New line for readability
        print("") 

    # Print the final score
    print(f"Game over. Your score is {user_score}/{total_questions}.")
    print("")