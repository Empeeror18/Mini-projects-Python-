import random

questions = \
    {
    "What is Black Panther’s real name?" : "T’Challa",
    "What is Iron Man's real name?" : "Tony Stark",
    "Who is the king of Asgard?" : "Odin",
    "Who is Thor’s brother?" : "Loki",
    "Which Avenger can turn into a green monster?" : "Hulk",
    "What is Captain America's shield made of?" : "Vibranium"
    }

def trivia_game():
    total_questions = 5
    question_list = list(questions.keys())
    score = 0

    selected_question = random.sample(question_list, total_questions) #Selects random 5 questions from questions list
    for idx, question in enumerate(selected_question):
        print(f"{idx + 1}. {question}")
        user_answer = input("Answer:").lower().strip()
        correct_answer = questions[question].lower() #Gets the answer

        if user_answer == correct_answer:
            print("✅Correct! \n")
            score += 1
        else:
            print(f"❌Wrong! The correct answer was {correct_answer}\n")

    print("*======================================*")
    print(f"Game Over! Your total score is: {score}/{total_questions}")
    print("*======================================*")

trivia_game()