mixed_questions = [
]

dict_question_input = {
}
def dict_question_form(dict_question):
    dict_question['question'] = []
    dict_question['answer'] = []
    dict_question['correct_index'] = []
    dict_question['score'] = []
def dict_question_list(dict_question):
    dict_question['question'].append(input("첫번째 문제 :"))
    dict_answer = []
    dict_answer.append(input("첫번째 답항 : "))
    dict_answer.append(input("두번째 답항 : "))
    dict_answer.append(input("세번째 답항 : "))
    dict_answer.append(input("네번째 답항 : "))
    dict_question['answer'].append(dict_answer)
    dict_question['correct_index'].append(input("정답 : "))
    dict_question['score'].append(input("점수 : "))
    mixed_questions.append(dict_question)

dict_question_form(dict_question_input)
for i in range(3):
    dict_question_list(dict_question_input)
pass
for dict_question in mixed_questions:
    question = dict_question['question']
    answer = dict_question['answer']
    correct_answer = dict_question['correct_index']
    score = dict_question['score']
for i in range(3):
    print("-------------------------------------")
    print('문제 : {}'.format(question[i]))
    print("첫번째 문항 : {}".format(answer[i][0]))
    print("두번째 문항 : {}".format(answer[i][1]))
    print("세번째 문항 : {}".format(answer[i][2]))
    print("네번째 문항 : {}".format(answer[i][3]))
    print("정답 : {}".format(correct_answer[i]))
    print("점수 : {}".format(score[i]))
    pass
