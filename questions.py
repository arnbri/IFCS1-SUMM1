# Import the random module to generate random numbers
import random

def generate_linear_equation():
    """
    Generates a linear equation in the form a + bx = y.

    Returns:
    alpha (int): a.
    beta (int): b.
    gamma (int): y.
    linear_eq_answer (int): The answer to the equation (x).
    """

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