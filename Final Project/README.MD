    # Testing Your Python Knowledge
    #### Video Demo:  <URL HERE>
    #### Description: 
    
    ##### What is this Project?
    This is a program that act as a Python quiz that tests your knowledge of fundamental Python concepts. It presents a series of multiple-choice questions, evaluates your answers, and provides feedback along with your final score.

    Function Breakdown:

    ##### 1. main() Function:

    --Serves as the program's entry point, executed when you run the script.
    --Prints a welcome message and quiz introduction.
    --Defines a list test_questions_options containing questions, answer choices, and correct answers.
    --Initializes empty lists user_input_response to store user responses and grade to track the score.
    --Iterates through each question using a loop:
        --Calls the make_question() function to display the question and answer choices.
        --Appends the user's answer to user_input_response.
        --Calls the user_answer_verification() function to check the answer and provide feedback.
        --If the answer is correct, increments the grade.
    --Calls the grade_calculator() function to determine the final score and display results.
    
    ##### 2. user_answer_verification() Function:

    --Takes three arguments: is_correct (Boolean indicating answer correctness), user_answer, and correct_answer.
    --Prints a message based on whether the answer was correct or incorrect.
    --Returns True for a correct answer, False otherwise (not used for anything in this code).
    
    ##### 3. grade_calculator() Function:

    --Takes two arguments: user_input_response (list of user answers) and test_questions_options (list of questions and answers).
    --Initializes a variable grade to 0.
    --Iterates through both lists simultaneously using zip():
        --Compares the user's answer with the corresponding question's correct answer.
        --If they match, increments the grade.
    --Calculates the percentage score by dividing the number of correct answers by the total number of questions and multiplying by 100.
    --Prints the score details and congratulatory messages based on the percentage range.
    --Returns the percentage score.
    
    ##### 4. make_question() Function:

    --Takes three arguments: problem (the question text), alternatives_answers (list of answer choices), and user (an optional input function, defaults to input).
    --Prints the question text.
    --Prints each answer choice from the provided list.
    --Prompts the user for their answer using user().
    --Creates a list acceptable_options containing lowercase versions of the first letters of each answer choice for validation.
    --Raises a ValueError if the user's input (converted to lowercase) is not among the valid answer letters (a, b, c, or d).
    --Returns the user's answer converted to lowercase.
    
    ##### Techniques that i used

    -> List Comprehensions: The code utilizes list comprehensions to create the acceptable_options list in the make_question() function, providing a concise way to generate a new list based on an existing one.
    -> String Formatting: The grade_calculator() function employs f-strings (introduced in Python 3.6) for formatted string output, making the score message more readable.
    -> Error Handling: The make_question() function demonstrates basic error handling by raising a ValueError if the user enters an invalid answer, ensuring the program's robustness.
    -> Iterating with zip(): The grade_calculator() function leverages zip() to iterate through two lists simultaneously, efficiently comparing user answers with their corresponding correct answers.
    