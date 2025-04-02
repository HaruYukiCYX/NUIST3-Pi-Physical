#Author: Chen Yuxuan
#Date: 2/4/2025
#Description: This code implements a simple animal quiz.

# NUIST Ouiz Game in Python
def quiz():
    print("Welcome to the Animal Quiz!")
    print("Answer the following questions:")
# Questions and Answers
questions =[
"1. What is the largest animal on Earth?: a. Blue Whale, b. Mouse, c. cat",
"2. Which bird can fly backwards?: a. Cuckoo, b. Eagle, c. Hummingbird ",
"3. What is the only mammal capable of flight?: a. Bat, b. squirrel, c. Dolphin " ]
answers = [
"blue whale",
"hummingbird",
"bat"]
score =0
# Ask questions
for i in range(len(questions)):
    user_answer = input(questions[i]).strip().lower()
    if user_answer == answers[i]:
        print("correct!")
        score += 1
    else:
        print("Incorrect!")
# Provide final score
print("\nOuiz completed!")
print(f"You got {score}/{len(questions)} questions correct.")
# Run the quiz function
quiz()
