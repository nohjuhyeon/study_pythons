# https://www.acmicpc.net/problem/11382
# 문제
## 꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!
# 입력
## 첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.
# 출력
## A+B+C의 값을 출력한다.

A, B, C = input().split()                   ## 입력을 몇개, 어떻게 할 것인가 

def question(A,B,C):                        # 입력한 값들을 어떻게 사용해서 결과값을 만들것인가
    answer = int(A) + int(B) + int(C)
    return answer

answer = question(A,B,C)

print(answer)                               ## 출력

# A = int(A)
# B = int(B)
# C = int(C)

# print(A+B+C)

# 입력한 값들을 어떻게 사용해서 결과값을 만들것인가























# def sum_three ():
#     A,B,C = map(int,input() .split()) #입력값 세 개를  변수로 지정
#     print(A + B + C)

# sum_three()