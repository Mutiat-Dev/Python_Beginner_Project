import json
import random

def main():
    questions = load_file()
    if questions == []:
        print("No questions available. Please check trivia.json")
        return

    random.shuffle(questions)
    user_answers = ask_questions(questions)

    final_score = check_answer(user_answers, questions)
    total = len(questions)
    print(f"\nYour final score is: {final_score}/{total}")
    result(final_score, total)

def load_file():
    try:
        with open("trivia.json", "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def ask_questions(questions):
    letters = ["a", "b", "c", "d"]
    user_answers = []

    for q in questions:
        print(q["question"])

        for index, option in enumerate(q["options"]):
                print(f"{letters[index]}. {option}")

        answer = input("\nWhat's your answer? ").strip().lower()
        while answer not in letters:
            print("Invalid input! Choose from a, b, c or d")
            answer = input("\nWhat's your answer? ").strip().lower()
        user_answers.append(answer)
    return user_answers

def check_answer(user_answers, questions):
    score = 0
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
    # print(score)
    return score

def result(final_score, total):
    percentage = final_score/total * 100
    if percentage <= 50:
        print("Average")
    elif percentage <= 70:
        print("Good Job!")
    elif percentage <= 100:
        print("Excellent Work!")
    else:
        print("You can do better!")

if __name__ == "__main__":
    while True:
        main()
        text = input("\nWould you like to play again? y/n ").strip().lower()
        while text not in ["y", "n"]:
            print("Invalid input. It's either y or n")
            text = input("\nWould you like to play again? y/n ").strip().lower()
        if text == "n":
            print("Thanks for playing!")
            break
