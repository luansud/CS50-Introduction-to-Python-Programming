def make_question(problem, alternatives_answers, user=input):
    print(problem)

    for option in alternatives_answers:
        print(option)

    user_input_response = user("Your answer: ", )

    acceptable_options = [option[0].lower() for option in alternatives_answers]
    if user_input_response.lower() not in acceptable_options:
        raise ValueError("You Should Type the letters: 'a, b, c, or d'")

    return user_input_response.lower()