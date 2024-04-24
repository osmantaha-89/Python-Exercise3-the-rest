print("Hello User")


def ask_question(question, answer):
    user_answer = input(question)
    return user_answer.strip() == answer

questions_and_answers = [
    ("What is 2 * 2? ", "4"),
    ("What is 6 / 3? ", "2"),
    ("What is 9 * 9? ", "81"),
]

for question, answer in questions_and_answers:
    if ask_question(question, answer):
        print("That is correct!") 
    else:
        print("That is false, you failed the test!")
        break
else:
    print("Correct! You passed the test!")
        
