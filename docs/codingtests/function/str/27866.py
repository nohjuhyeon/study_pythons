# https://www.acmicpc.net/problem/27866
# 문제
## 단어 S와 정수 i가 주어졌을 때, S의 i번째 글자를 출력하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 S가 주어진다. 단어의 길이는 최대 $1,000$이다.
## 둘째 줄에 정수 i가 주어진다. (1 <= i <= |S|)
# 출력
## S의 i번째 글자를 출력한다.

def str_index_find(str_input):
    index = int(input()) - 1            # 추출할 문자의 인덱스 입력
    str_index = str_input[index]        # 문자 추출₩                                                    
    return str_index

str_input = input()
str_index = str_index_find(str_input)
print(str_index)