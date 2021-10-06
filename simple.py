TECH = "question_pools/techclass20182022.json"
GENERAL = "question_pools/generalclass20192023.json"
EXTRA = "question_pools/extraclass20202024.json"

import json

def readFile(filename):
    raw = open(filename, 'r')
    data = json.loads(raw.read())
    raw.close()
    return data

def parseAnswer(question, class_level):
    question_id = question['id']
    if class_level == 'tech':
        question_id = question_id.split('(')
        return question_id[1][0:1].lower()

def runQuiz(question_pool):
    SCORE = 0
    TOTAL_SCORE = 0
    for question in question_pool:
        TOTAL_SCORE += 1
        print(question['question'])
        for letter in ['a', 'b', 'c', 'd', 'e']:
            if letter in question:
                print("\t" + letter + ' - ' + question[letter])
        user_answer = input(" > ").lower()
        correct_answer = parseAnswer(question, 'tech')
        if user_answer == correct_answer:
            SCORE += 1
            print("Correct!")
        else:
            print("Incorrect.  The correct answer was:")
            print(correct_answer + " - " + question[correct_answer])
        print("Score: " + str(SCORE) + " out of " + str(TOTAL_SCORE))
        print("\n")

if __name__ == '__main__':
    current_class = TECH

    print("Starting simple Python quiz for " + current_class + "....\n")
    question_pool = readFile(current_class)
    runQuiz(question_pool)
    