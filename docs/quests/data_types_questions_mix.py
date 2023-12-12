mixed_questions = [

]

dict_question_input = {
    'question': [],
    'answer_first': [],
    'answer_second': [],
    'answer_third': [],
    'answer_fourth': [],
    'correct_index': [],
    'score': []
}


def dict_question_form(dict_question):
    dict_question['question'].append(input("첫번째 문제 :"))
    dict_question['answer_first'].append(input("첫번째 답항 : "))
    dict_question['answer_second'].append(input("두번째 답항 : "))
    dict_question['answer_third'].append(input("세번째 답항 : "))
    dict_question['answer_fourth'].append(input("네번째 답항 : "))
    dict_question['correct_index'].append(input("정답 : "))
    dict_question['score'].append(input("점수 : "))
    mixed_questions.append(dict_question)
for i in range(3):
    dict_question_form(dict_question_input)
pass
for dict_question in mixed_questions:
    question = dict_question['question']
    answer_first = dict_question['answer_first']
    answer_second = dict_question['answer_second']
    answer_third = dict_question['answer_third']
    answer_fourth = dict_question['answer_fourth']
    correct_answer = dict_question['correct_index']
    score = dict_question['score']
for i in range(3):
    print("-------------------------------------")
    print('문제 : {}'.format(question[i]))
    print("첫번째 문항 : {}".format(answer_first[i]))
    print("두번째 문항 : {}".format(answer_second[i]))
    print("세번째 문항 : {}".format(answer_third[i]))
    print("네번째 문항 : {}".format(answer_fourth[i]))
    print("정답 : {}".format(correct_answer[i]))
    print("점수 : {}".format(score[i]))
    pass
