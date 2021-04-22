# Open the raw (yet cleaned up) question pool
raw = open('question_pools/techclass20182022.txt', 'r')
data = raw.read()
raw.close()

# Split apart by questions, add to dictionary
question_pool = {}
questions = data.split("~~")
print("-" + questions[0] + "-")
print("-" + questions[1] + "-")
print(questions[2])
x = 0
while x < len(questions):
    questions[x] = questions[x].split('\n')
    questions[x].pop(len(questions[x]) - 1)

    # Parse out the question ID, answer, and reference number
    id_answer_ref = questions[x][1].split(' ')
    answer = id_answer_ref[1][1:2]
    ref = id_answer_ref[2][1:len(id_answer_ref[2])-1]

    # Parse out the question
    single_question = questions[x][2]

    # Parse out the possible answers
    answers = questions[x][3:]
    
    # Add to question pool
    question_pool[id] = {
        'correct_answer': answer,
        'possible_answers': answers,
        'question': single_question,
        'reference_num': ref
    }
    x+=1

# print(question_pool)