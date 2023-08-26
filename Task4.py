# QUIZ GAME USING PYTHON #

import random
import time

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class MultipleChoiceQuestion(Question):
    def __init__(self, question, choices, correct_choice):
        super().__init__(question, correct_choice)
        self.choices = choices

class FillInTheBlankQuestion(Question):
    def __init__(self, question, correct_answer):
        super().__init__(question, correct_answer)

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def run(self):
        random.shuffle(self.questions)
        for index, question in enumerate(self.questions, start=1):
            print(f"Question {index}/{len(self.questions)}:")
            print(question.question)

            if isinstance(question, MultipleChoiceQuestion):
                for i, choice in enumerate(question.choices, start=1):
                    print(f"{i}. {choice}")
                
                user_choice = input("Enter your answer (1, 2, 3, 4): ")
                if user_choice.isdigit():
                    user_choice = int(user_choice) - 1
                    if 0 <= user_choice < len(question.choices):
                        if question.choices[user_choice] == question.answer:
                            print("Correct!\n")
                            self.score += 1
                        else:
                            print(f"Wrong! The correct answer is: {question.answer}\n")
                    else:
                        print("Invalid choice.\n")
                else:
                    print("Invalid input.\n")
            else:  # Fill-in-the-blank question
                user_answer = input("Enter your answer: ")
                if user_answer.lower() == question.answer.lower():
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is: {question.answer}\n")
            
            # time delay before showing the next question
            time.sleep(1)
        
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")
        if self.score >= 7 :
            print("EXCELLENT...Keep It Up!!!!")
        elif self.score < 7 and self.score > 4:
            print("Not that Bad...keep trying!!")
        else:
            print("Work Hard on Your Mythological Skills Dude!!!") 
        self.score = 0               

# Question instances
questions = [
    MultipleChoiceQuestion("How many Chiranjeevis are there?", ["9", "5", "10", "7"], "7"),
    MultipleChoiceQuestion("How many Divine Yugas are there?", ["1", "2", "3", "4"], "4"),
    MultipleChoiceQuestion("How many Avatars are there of Vishnu in the divine yugas?", ["11", "5", "10", "7"], "10"),
    MultipleChoiceQuestion("What is the coorect order of Vishnu avatars in the four yugas?", ["4,3,2,1", "1,2,3,4", "3,2,4,1", "4,2,1,3"], "4,3,2,1"),
    MultipleChoiceQuestion("What is the name of the second Yuga?", ["Satya-yuga", "Treta-yuga", "Kali-yuga", "Dvaapar-yuga"], "Treta-yuga"),
    MultipleChoiceQuestion("Who used Brahmastra in Mahabharata to end the Pandava's Dynasty?", ["Ashwatthama", "Bhishma", "Arjuna", "Karan"], "Ashwatthama"),
    MultipleChoiceQuestion("Who told Hanumana about the Sanjeevni Booti?", ["Vibhishana", "Rama", "Sushen", "Lakshmana"], "Sushen"),
    MultipleChoiceQuestion("Who was the first ever human being created by Brahma?", ["Dhruv", "Manu", "Shatrupa", "Vishnugupt"], "Manu"),
    FillInTheBlankQuestion("_____ was the father of Kauravas?", "Dhritarashtra"),
    FillInTheBlankQuestion("_____ avatar of Vishnu would be there in Kaliyug?", "Kalki")
    
]

# QuizGame instance and start the game
time.sleep(1.5)
print("---------------------------------WELCOME TO THE QUIZ GAME---------------------------------")
time.sleep(2.5)
print("_______________________________________HINDU MYTHOLOGY_______________________________________")
time.sleep(2.5)
print("__________________If you believe it as a MYTH then its a MYTHOLOGY for you!!__________________")
time.sleep(5)
print("_________________But if you believe it as TRUTH then its a SATYALOGY for you!!_________________")
time.sleep(5)
print("______________READY TO DIVE INTO THE MOST EXCLUSIVE QUIZ ABOUT HINDU MYTHOLOGY???______________")
time.sleep(5)
print("__________________________________________LET'S GO!__________________________________________")
time.sleep(2.5)
print("_______________There will be 10 questions randomly of either MCQ's and Fill-ups_______________")
time.sleep(2.5)
quiz = QuizGame(questions)
while(True):
    quiz.run()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower()!= "y":
        break

