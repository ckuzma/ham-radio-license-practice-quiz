TECH = "question_pools/techclass20182022.json"
GENERAL = "question_pools/generalclass20192023.json"
EXTRA = "question_pools/extraclass20202024.json"

import json
import os
import random

def readFile(filename):
    raw = open(filename, 'r')
    data = json.loads(raw.read())
    raw.close()
    return data

def parseAnswer(question):
    question_id = question['id'].split('(')
    return question_id[1][0:1].lower()

def runQuiz(question_pool):
    SCORE = 0
    TOTAL_SCORE = 0
    while True:
        question = question_pool[random.randrange(0, len(question_pool)+1)]
        TOTAL_SCORE += 1
        print(question['question'])
        for letter in ['a', 'b', 'c', 'd', 'e']:
            if letter in question:
                print("\t" + letter + ' - ' + question[letter])
        user_answer = input(" > ").lower()
        correct_answer = parseAnswer(question)
        if user_answer == correct_answer:
            SCORE += 1
            print("Correct!")
        else:
            print("Incorrect.  The correct answer was:")
            print(correct_answer + " - " + question[correct_answer])
        print("Score: " + str(SCORE) + " out of " + str(TOTAL_SCORE))
        print("\n")
        input("Press ENTER to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    print("Starting simple Python quiz.")
    print("Press CTRL + C at any time to quit.\n")
    print("Choose a class level:\n\t1. Tech\n\t2. General\n\t3. Extra")
    current_class = int(input(" > "))
    if current_class == 1:
        current_class = TECH
    if current_class == 2:
        current_class = GENERAL
    if current_class == 3:
        current_class = EXTRA
    
    print("\nOpening question pool: " + current_class + "\n")
    question_pool = readFile(current_class)
    runQuiz(question_pool)