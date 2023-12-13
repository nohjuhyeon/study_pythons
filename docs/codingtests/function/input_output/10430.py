# https://www.acmicpc.net/problem/10430
# 문제
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
# 출력
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.


num_A,num_B,num_C = map(int, input() .split())              #입력값들을 변수 A,B,C로 지정


def operation_first(num_A,num_B,num_C):                     #첫번째 계산식 함수 지정
    print((num_A + num_B) % num_C)
def operation_second(num_A,num_B,num_C):                    #두번쨰 계산식 함수 지정
    print(((num_A % num_C) + (num_B % num_C)) % num_C)
def operation_third(num_A,num_B,num_C):                     #세번째 계산식 함수 지정
    print((num_A * num_B) % num_C)
def operation_fourth(num_A,num_B,num_C):                    #네번째 계산식 함수 지정
    print(((num_A % num_C) * (num_B % num_C)) % num_C)

operation_first(num_A,num_B,num_C)
operation_second(num_A,num_B,num_C)
operation_third(num_A,num_B,num_C)
operation_fourth(num_A,num_B,num_C)