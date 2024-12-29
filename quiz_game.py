def main():
    print("Welcome to My Computer Quiz!")

    playing = input("Do you want to play? ").lower()

    if playing not in ["yes","y"]:
        quit()

    print("Okay! Lets play :)")
    questions = ["CPU","E-mail","WWW","GPU", "RAM", "ROM", "PC", "OS", "DOC", "MS"]
    answers = ["central processing unit", "electronic mail", "world wide web", 
    "graphics processing unit", "random access memory", "read only memory", 
    "personal computer", "operating system", "document", "microsoft"]

    number_of_questions = int(input("How many questions do you want to answer (there are 10 queztions)? "))
    print("You will get 5 points for each correct answer and -2 points for each incorrect answer.")
    total_score = 0
    correct_count = 0
    incorrect_count = 0

    print(f"Answer {number_of_questions} quiz questions!")

    for ques_no in range(number_of_questions):
        print(f"Question Number: {ques_no+1}")
        answer = input(f"What does {questions[ques_no]} stand for: ").lower()
        if answer == answers[ques_no]:
            print("Correct! you earned 5 points.")
            correct_count += 1
            total_score += 5
        else:
            print("Incorrect! you lost 2 points.")
            incorrect_count += 1
            total_score -= 2
        print(f"Your current score is {total_score} and you got {correct_count} questions correct.")

    print(f"You got {((total_score/number_of_questions) * 100):.2f}%.")
    print(f"Your final score {total_score}")

if __name__ == "__main__":
    main()
