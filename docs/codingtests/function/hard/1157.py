# https://www.acmicpc.net/problem/1157
# 문제
## 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력
## 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력
## 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

str_input = input().upper()                             # 입력한 문자를 대문자로 변경

def count_str(str_input):
    set_input = set(str_input)                          
    list_input = list(set_input)                        # 중복된 문자 빼고 리스트 구성
    list_count = []
    for i in range(len(list_input)):                    # 리스트 길이 만큼 반복
        str_count = str_input.count(list_input[i])      # 문자마다 개수 확인
        list_count.append(str_count)                    # 문자마다 개수를 기록한 리스트 작성
    max_index = list_count.index(max(list_count))       # 가장 많은 개수의 인덱스 찾기
    pass
    if list_count.count(max(list_count)) == 1:          # 만약 카운트 리스트에서 최고값이 하나일 경우 그 값의 문자 출력
        print(list_input[max_index])
    else:
        print("?")                                      # 아닐 경우 "?"출력
    pass


count_str(str_input)