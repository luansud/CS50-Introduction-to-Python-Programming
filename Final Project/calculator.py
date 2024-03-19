def grade_calculator(user_input_response, test_questions_options):
    grade = 0
    for user_answer, i in zip(user_input_response, test_questions_options):
        if user_answer == i["correct_answer"]:
            grade += 1

    total_problems = len(test_questions_options)
    grade_in_percent = (grade / total_problems) * 100
    print(f"You got {grade} of {total_problems} questions")
    if grade_in_percent == 100:
        print("Congratulations, you got a perfect grade!")
    elif grade_in_percent < 99 and grade_in_percent >= 80:
        print("Well Done, You did a great job!")
    elif grade_in_percent < 79 and grade_in_percent >= 60:
        print("Good, but i know that you can do better!")
    else:
        print("Keep trying!")
        
    return grade_in_percent