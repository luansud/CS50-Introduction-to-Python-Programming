from calculator import grade_calculator
from feedback import user_answer_verification
from question import make_question

def main():
    print("This Quiz will test your Knowledge about Python!\n")
    print("Now you have the opportunity to verify if you understood the subject!\n")
    print("---------------------Python Basic Test------------------------")

    test_questions_options = [
        {"problem": "What is the correct extension for Python files?", "alternatives": ["a) .pi", "b) .p", "c) .py", "d) .python"], "correct_answer": "c"},
        {"problem":"What is a correct syntax to output 'Hello World' in Python?", "alternatives": ["a) p('Hello World')", "b) print('Hello World')", "c) echo 'Hello World'", "d) echo('Hello World')"], "correct_answer": "b"},
        {"problem": "Which one is NOT a legal variable name?", "alternatives": ["a) my_var", "b) Myvar", "c) _myvar", "d) my-var"], "correct_answer": "d"},
        {"problem": "Which method can be used to remove any whitespace from both the beginning and the end of a string?", "alternatives": ["a) trim()", "b) strip()", "c) split()", "d) len()"], "correct_answer": "b"},
        {"problem": "Which method can be used to replace parts of a string?", "alternatives": ["a) switch()", "b) repl()", "c) replaceString()", "d) replace()"], "correct_answer": "d"},
        {"problem": "Which method can be used to return a string in upper case letters?", "alternatives": ["a) upper()", "b) uppercase()", "c) toUpperCase()", "d) upperCase()"], "correct_answer": "a"},
        {"problem": "Key words such as true and false are ___.", "alternatives": ["a) lower case", "b) UPPER CASE", "c) Capitalized", "d) italicized"], "correct_answer": "c"},
        {"problem": "Which of these collections defines a LIST?", "alternatives": ['a)  ["apple", "banana", "cherry"]', 'b)  {"name": "apple", "color": "green"}', 'c)  ("apple", "banana", "cherry")', 'd)  {"apple", "banana", "cherry"}'], "correct_answer": "a"},
        {"problem": "Which collection is ordered, changeable, and allows duplicate members?", "alternatives": ["a) TUPLE", "b) DICTIONARY", "c) LIST", "d) SET"], "correct_answer": "c"},
        {"problem": "Which collection does not allow duplicate members?", "alternatives": ["a) TUPLE", "b) DICTIONARY", "c) LIST", "d) SET"], "correct_answer": "d"},        
        {"problem": "Which statement is used to stop a loop?", "alternatives": ["a) stop", "b) exit", "c) return", "d) break"], "correct_answer": "d"},
        {"problem": "How do you start writing a while loop in Python?", "alternatives": ["a) while x > y:", "b) while > y {", "c) while (x>y)", "d) x > y while{"], "correct_answer": "a"},
        {"problem": "Which keyword is used for functions in Python?", "alternatives": ["a) def", "b) function", "c) define", "d) fun"], "correct_answer": "a"},
        {"problem": "What does OOP stand for?", "alternatives": ["a) other-object programming", "b) object-oriented programming", "c) object-orientation programming", "d) none of the mentioned"], "correct_answer": "b"},
        {"problem": "What is the construct called for creating anonymous functions?", "alternatives": ["a) anonymous", "b) lambda", "c) pi", "d) llama"], "correct_answer": "b"}
    ]

    user_input_response =[]
    grade = 0
    for i in test_questions_options:
        user_answer = make_question(i["problem"], i["alternatives"])
        user_input_response.append(user_answer)
        is_correct = user_answer == i["correct_answer"]
        user_answer_verification(is_correct, user_answer, i["correct_answer"])
        if is_correct:
            grade += 1
    grade_calculator(user_input_response, test_questions_options)
    
if __name__ == "__main__":
    main()