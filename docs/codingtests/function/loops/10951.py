# https://www.acmicpc.net/problem/10951
# 문제
## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
## 입력은 여러 개의 테스트 케이스로 이루어져 있다.
## 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
## 각 테스트 케이스마다 A+B를 출력한다.

def sum():
    num_A,num_B = map(int, input().split())                             # num_A, num_B 입력
    while True:
        try:
            print(num_A + num_B)                                        # num_A, num_B 의 합 출력
            num_A,num_B = map(int, input().split())                     # num_A, num_B 입력
        except:                                                         # 문제가 발생할 경우 break
            break

sum()