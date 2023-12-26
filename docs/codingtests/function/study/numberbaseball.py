# 첫번째 줄에 숫자 3개를 입력한다. 
# 두번째 줄에 도전 횟수를 입력한다. 
# 세번째 줄 부터 맞추는 기회가 주어진다. 

# - 숫자는 맞지만 위치가 틀렸을 때는 볼
# - 숫자와 위치가 전부 맞으면 스트라이크
# - 숫자와 위치가 전부 틀리면 아웃이 주어진다. 
# - 만약 모두 틀렸을 경우 '아웃'이 출력된다.

# 선택 사항)
# - 3S가 나올 경우 프로그램 종료
# - 입력 양식이 틀릴 경우 다시 입력
# - 숫자 3개 입력 시 값 중에 똑같은 값이 있을 경우 다시 입력

# 예시)
# 입력
# - 076
# - 5 
# - 485
# - 310
# - 206
# - 067
# - 076

# 출력
# - 아웃
# - 0S 1B
# - 1S 1B
# - 1S 2B
# - 3S 0B

list_number = [0,1,2,3,4,5,6,7,8,9]                                                                                                      # 입력 값과 비교할 리스트 설정
print("숫자를 3개 입력하세요.")                                                    
list_question =list(map(int, input("입력 : ").split()))                                                                                      # 입력한 값을 리스트로 변환
num_chance = int(input("도전 횟수 입력 : "))                                                                                             # 도전 횟수 입력
for i in range(num_chance):                                                                                                             # 도전 횟수 만큼 반복
    count_strike = 0                                                                                                                    # 스트라이크를 세주는 변수 지정
    count_ball = 0                                                                                                                      # 볼을 세주는 변수 지정
    list_answer =list(map(int, input("입력 : ").split()))                                                                                      # 입력한 값을 리스트로 변환
    for j in range(len(list_answer)):                                                                                                   # 답안지의 
        for k in range(len(list_question)):
            if list_answer[j] == list_question[k]:                                                                                      # 답지가 질문지 내에 있을 경우
                if j == k:                                                                                                              # 만약 인덱스 번호가 같을 경우
                    count_strike += 1                                                                                                   # 스트라이크 + 1
                else:                                                                                                                   # 만약 인덱스 번호가 다를 경우
                    count_ball += 1                                                                                                     # 볼 + 1
            else:
                pass
    if count_strike == 3:                                                                                                               # 3스트라이크일 경우
        print("{}S {}B (남은 기회 : {})".format(count_strike,count_ball, num_chance - i - 1))                                            
        break                                                                                                                           # 반복문 종료
    elif count_strike == 0 and count_ball == 0:                                                                                         # 스트라이크와 볼이 모두 0일 경우
        print("아웃 (남은 기회 : {})".format(num_chance - i - 1))                                                                        # 아웃
    else:                                                                                                                               # 둘 다 아닐 경우 스트라이크와 볼 갯수 출력후 반복
        print("{}S {}B (남은 기회 : {})".format(count_strike,count_ball, num_chance - i - 1))
if count_strike == 3:
    print("정답입니다!")
else:
    print("GAME OVER")




# list_number = [0,1,2,3,4,5,6,7,8,9]                                                                                                      # 입력 값과 비교할 리스트 설정
# print("숫자를 3개 입력하세요.")                                                    
# while True:                                                                                                                                   # 원하는 값이 입력 될 때 까지 반복
#     list_question =list(map(int, input("입력 : ").split()))                                                                                      # 입력한 값을 리스트로 변환
#     pass
#     try:    
#         if len(list_question) != 3:                                                                                                              # 입력한 값으로 구성된 리스트가 3개가 아닐 경우 다시 입력 
#             print("숫자를 3개 입력하세요.")
#             pass
#         else:
#             if list_question[0] != list_question[1] and list_question[0] != list_question[2] and list_question[2] != list_question[1]:                    # 입력한 값들이 서로 겹치는지 비교
#                 list_check = 0
#                 for i in range(len(list_question)):
#                     num_check = 1                                                                                                       # 입력 한 값이 0-9 사이인지 확인하기 위한 수단 제공
#                     for j in range(len(list_number)):                                                                              
#                         if list_question[i] == list_number[j]:                                                                        # 입력한 값이 0-9 사이에 있을 경우
#                             num_check = num_check * 0                                                                                   # num_check에 0을 곱해 0으로 만들기
#                     list_check += num_check                                                                                             # list_check에 num_check 더하기
#                 pass
#                 if list_check == 0:                                                                                                     # list_check가 0일 경우 모든 값들이 0-9 사이에 있다는 뜻이므로 반복문 종료
#                     break
#                 else:                                                                                                                   # 0이 아닐 경우 다시 입력
#                     print("0-9 사이의 숫자를 입력하세요.")
#                     pass
                    
#             else:                                                                                                                       # 입력한 값들이 서로 겹칠 경우 다시 입력
#                 print("값이 다른 숫자 3개를 입력하세요.")
#                 pass
#             pass
#     except:                                                                                                                             # 오류가 날 경우 다시 입력
#         print("숫자를 3개 입력하세요.")
#         pass    
# num_chance = int(input("도전 횟수 입력 : "))                                                                                             # 도전 횟수 입력
# for i in range(num_chance):                                                                                                             # 도전 횟수 만큼 반복
#     count_strike = 0                                                                                                                    # 스트라이크를 세주는 변수 지정
#     count_ball = 0                                                                                                                      # 볼을 세주는 변수 지정
#     while True:                                                                                                                                   # 원하는 값이 입력 될 때 까지 반복
#         list_answer =list(map(int, input("입력 : ").split()))                                                                                      # 입력한 값을 리스트로 변환
#         pass
#         try:    
#             if len(list_answer) != 3:                                                                                                              # 입력한 값으로 구성된 리스트가 3개가 아닐 경우 다시 입력 
#                 print("숫자를 3개 입력하세요.")
#                 pass
#             else:
#                 if list_answer[0] != list_answer[1] and list_answer[0] != list_answer[2] and list_answer[2] != list_answer[1]:                    # 입력한 값들이 서로 겹치는지 비교
#                     list_check = 0
#                     for j in range(len(list_answer)):
#                         num_check = 1                                                                                                       # 입력 한 값이 0-9 사이인지 확인하기 위한 수단 제공
#                         for k in range(len(list_number)):                                                                              
#                             if list_answer[j] == list_number[k]:                                                                        # 입력한 값이 0-9 사이에 있을 경우
#                                 num_check = num_check * 0                                                                                   # num_check에 0을 곱해 0으로 만들기
#                         list_check += num_check                                                                                             # list_check에 num_check 더하기
#                     pass
#                     if list_check == 0:                                                                                                     # list_check가 0일 경우 모든 값들이 0-9 사이에 있다는 뜻이므로 반복문 종료
#                         break
#                     else:                                                                                                                   # 0이 아닐 경우 다시 입력
#                         print("0-9 사이의 숫자를 입력하세요.")
#                         pass
                        
#                 else:                                                                                                                       # 입력한 값들이 서로 겹칠 경우 다시 입력
#                     print("값이 다른 숫자 3개를 입력하세요.")
#                     pass
#                 pass
#         except:                                                                                                                             # 오류가 날 경우 다시 입력
#             print("숫자를 3개 입력하세요.")
#             pass                                                                                 # 답안지 입력
#     for j in range(len(list_answer)):                                                                                                 
#         for k in range(len(list_question)):
#             if list_answer[j] == list_question[k]:                                                                                      # 답지가 질문지 내에 있을 경우
#                 if j == k:                                                                                                              # 만약 인덱스 번호가 같을 경우
#                     count_strike += 1                                                                                                   # 스트라이크 + 1
#                 else:                                                                                                                   # 만약 인덱스 번호가 다를 경우
#                     count_ball += 1                                                                                                     # 볼 + 1
#     pass
#     if count_strike == 3:                                                                                                               # 3스트라이크일 경우
#         print("{}S {}B (남은 기회 : {})".format(count_strike,count_ball, num_chance - i - 1))                                            
#         break                                                                                                                           # 반복문 종료
#     elif count_strike == 0 and count_ball == 0:                                                                                         # 스트라이크와 볼이 모두 0일 경우
#         print("아웃 (남은 기회 : {})".format(num_chance - i - 1))                                                                        # 아웃
#     else:                                                                                                                               # 둘 다 아닐 경우 스트라이크와 볼 갯수 출력후 반복
#         print("{}S {}B (남은 기회 : {})".format(count_strike,count_ball, num_chance - i - 1))
# if count_strike == 3:
#     print("정답입니다!")
# else:
#     print("GAME OVER")

















# class quest: 
#     def __init__(self):
#         self.list_number = [0,1,2,3,4,5,6,7,8,9]                                                                                                      # 입력 값과 비교할 리스트 설정

#     def input_list(self):
#         print("숫자를 3개 입력하세요.")                                                    
#         while True:                                                                                                                                   # 원하는 값이 입력 될 때 까지 반복
#             list_input =list(map(int, input("입력 : ").split()))                                                                                      # 입력한 값을 리스트로 변환
#             pass
#             try:    
#                 if len(list_input) != 3:                                                                                                              # 입력한 값으로 구성된 리스트가 3개가 아닐 경우 다시 입력 
#                     print("숫자를 3개 입력하세요.")
#                     pass
#                 else:
#                     if list_input[0] != list_input[1] and list_input[0] != list_input[2] and list_input[2] != list_input[1]:                    # 입력한 값들이 서로 겹치는지 비교
#                         list_check = 0
#                         for i in range(len(list_input)):
#                             num_check = 1                                                                                                       # 입력 한 값이 0-9 사이인지 확인하기 위한 수단 제공
#                             for j in range(len(self.list_number)):                                                                              
#                                 if list_input[i] == self.list_number[j]:                                                                        # 입력한 값이 0-9 사이에 있을 경우
#                                     num_check = num_check * 0                                                                                   # num_check에 0을 곱해 0으로 만들기
#                             list_check += num_check                                                                                             # list_check에 num_check 더하기
#                         pass
#                         if list_check == 0:                                                                                                     # list_check가 0일 경우 모든 값들이 0-9 사이에 있다는 뜻이므로 반복문 종료
#                             break
#                         else:                                                                                                                   # 0이 아닐 경우 다시 입력
#                             print("0-9 사이의 숫자를 입력하세요.")
#                             pass
                            
#                     else:                                                                                                                       # 입력한 값들이 서로 겹칠 경우 다시 입력
#                         print("값이 다른 숫자 3개를 입력하세요.")
#                         pass
#                     pass
#             except:                                                                                                                             # 오류가 날 경우 다시 입력
#                 print("숫자를 3개 입력하세요.")
#                 pass
#         return list_input
    
#     def answer_input(self,list_question):                                                                                                       # 외부에서 첫번째 줄에서 입력한 리스트 가져오기
#         num_chance = int(input("도전 횟수 입력 : "))                                                                                             # 도전 횟수 입력
#         for i in range(num_chance):                                                                                                             # 도전 횟수 만큼 반복
#             count_strike = 0                                                                                                                    # 스트라이크를 세주는 변수 지정
#             count_ball = 0                                                                                                                      # 볼을 세주는 변수 지정
#             list_answer = self.input_list()                                                                                                     # 답안지 입력
#             for j in range(len(list_question)):                                                                                                 
#                 for k in range(len(list_question)):
#                     if list_answer[j] == list_question[k]:                                                                                      # 답지가 질문지 내에 있을 경우
#                         if j == k:                                                                                                              # 만약 인덱스 번호가 같을 경우
#                             count_strike += 1                                                                                                   # 스트라이크 + 1
#                         else:                                                                                                                   # 만약 인덱스 번호가 다를 경우
#                             count_ball += 1                                                                                                     # 볼 + 1
#             if count_strike == 3:                                                                                                               # 3스트라이크일 경우
#                 print("{}S {}B (남은 기회 : {})".format(count_strike,count_ball, num_chance - i - 1))                                            
#                 break                                                                                                                           # 반복문 종료
#             elif count_strike == 0 and count_ball == 0:                                                                                         # 스트라이크와 볼이 모두 0일 경우
#                 print("아웃 (남은 기회 : {})".format(num_chance - i - 1))                                                                        # 아웃
#             else:                                                                                                                               # 둘 다 아닐 경우 스트라이크와 볼 갯수 출력후 반복
#                 print("{}S {}B (남은 기회 : {})".format(count_strike,count_ball, num_chance - i - 1))
#         if count_strike == 3:
#             print("정답입니다!")
#         else:
#             print("GAME OVER")

# Quest = quest()                                                                                                                                
# list_question = Quest.input_list()                                                                                                             # 질문지 입력
# Quest.answer_input(list_question)                                                                                                              # 게임 진행