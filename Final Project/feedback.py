def user_answer_verification(is_correct, user_answer, correct_answer):
    if is_correct:
        print("----------- Correct answer! -----------")
        return True
    else:
        print("----------- Incorrect answer! -----------")
        return False