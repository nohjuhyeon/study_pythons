mixed_questions = [

]

dict_question_first = {
    'question': "",
    'answer': [],
    'correct_index': "",
    'score': ""
}
dict_question_second = {
    'question': "",
    'answer': [],
    'correct_index': "",
    'score': ""
}
dict_question_third = {
    'question': "",
    'answer': [],
    'correct_index': "",
    'score': ""
}

def dict_question_form(dict_question):
    dict_question['question'] = input("첫번째 문제 :")
    dict_question['answer'].append(input("첫번째 답항 : "))
    dict_question['answer'].append(input("두번째 답항 : "))
    dict_question['answer'].append(input("세번째 답항 : "))
    dict_question['answer'].append(input("네번째 답항 : "))
    dict_question['correct_index'] = input("정답 : ")
    dict_question['score'] = input("점수 : ")
    mixed_questions.append(dict_question)
print(dict_question_first)

dict_question_form(dict_question_first)
dict_question_form(dict_question_second)
dict_question_form(dict_question_third)
pass
for dict_question in mixed_questions:
    question = dict_question['question']
    answer_first = dict_question['answer'][0]
    answer_second = dict_question['answer'][1]
    answer_third = dict_question['answer'][2]
    answer_fourth = dict_question['answer'][3]
    correct_answer = dict_question['correct_index']
    score = dict_question['score']
    print('문제 : {}'.format(question))
    print("첫번째 문항 : {}".format(answer_first))
    print("두번째 문항 : {}".format(answer_second))
    print("세번째 문항 : {}".format(answer_third))
    print("네번째 문항 : {}".format(answer_fourth))
    print("정답 : {}".format(correct_answer))
    print("점수 : {}".format(score))
    pass
