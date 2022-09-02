# ------------------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)

        guess = input("Enter (A, B or C): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# ------------------------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return
    else:
        print("WORNG!")
        return 0
# ------------------------------------------

def display_score(correct_guesses, guesses):

    print("----------------------------------------")
    print("Results")
    print("----------------------------------------")
    print("Answer: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is:"+str(score)+"%")
# ------------------------------------------
def play_again():
    pass
# ------------------------------------------


questions = {
          "Who create a python?:": "A",
          "What year was Python create?: ": "B",
          "Python is tributed to which comedy group?:": "C"
          }

options = [["A . Guido van Rossum", "B. Mark zuckbuurg ", "C . Bill gates ", "D . Ambani"],
           ["A . 1899", "B . 1991", "C . 2003", "D . 2008"],
           ["A . lovely Island ", "B . Smosh ", "C . Monty Python", "D . Kumar"]]


new_game()
