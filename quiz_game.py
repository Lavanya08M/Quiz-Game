def main():
    # Print welcome statement
    print("\"Welcome to My Computer Quiz!\"")

    # Ask the user whether he/she wants to play the game or not
    playing = input("Do you want to play? ").lower()

    # Check if the playing variable is yes or y or else quit the game
    if playing not in ["yes","y"]:
        quit()

    # If player says yes then start the quiz game
    print("Okay! Lets play :)")

    # Store questions and answers in a dictionaty
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

    # Ask the user how many questions he want to answer in quiz
    number_of_questions = int(input("How many questions do you want to answer (there are 10 queztions)? "))

    # Give a note about points he/she will get for correct and incoorect answers
    print("\n\"Note: You will get 5 points for each correct answer and -2 points for each incorrect answer.\"\n")

    # Store total score of the player in the total_score variable
    total_score = 0

    # count of correct and incorrect answers
    correct_count = 0
    incorrect_count = 0
    ques_no = 1


    print(f"Answer below {number_of_questions} questions in Quiz!\n")

 
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
