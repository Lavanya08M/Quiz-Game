def main():
    print("\"Welcome to My Computer Quiz!\"")

    playing = input("Do you want to play? ").lower()

    if playing not in ["yes","y"]:
        quit()

    print("Okay! Lets play :)")

    quiz_dict = {
        "CPU": "central processing unit",
        "E-mail": "electronic mail",
        "WWW": "world wide web",
        "GPU": "graphics processing unit", 
        "RAM": "random access memory", 
        "ROM": "read only memory", 
        "PC": "personal computer", 
        "OS": "operating system", 
        "DOC": "document", 
        "MS": "microsoft"
    }

    number_of_questions = int(input("How many questions do you want to answer (there are 10 queztions)? "))

    print("\n\"Note: You will get 5 points for each correct answer and -2 points for each incorrect answer.\"\n")

    total_score = 0
    correct_count = 0
    incorrect_count = 0
    ques_no = 1

    print(f"Answer {number_of_questions} quiz questions!")

 
    for ques, ans in quiz_dict.items():
        if ques_no > number_of_questions:
            break
        print(f"Question Number: {ques_no}")
        answer = input(f"What does {ques} stand for: ").lower()
        if answer == ans:
            print("Correct! you earned 5 points.")
            correct_count += 1
            total_score += 5
        else:
            print("Incorrect! you lost 2 points.")
            incorrect_count += 1
            total_score -= 2
        ques_no += 1
        print(f"Your got {correct_count} correct and {incorrect_count} incorrect.")

    print(f"You got {((correct_count/number_of_questions) * 100):.2f}%.")
    print(f"Your final score \"{total_score}\" points")

if __name__ == "__main__":
    main()
