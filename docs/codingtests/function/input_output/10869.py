# https://www.acmicpc.net/problem/10869
# 문제
## 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
# 입력
## 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# 출력
## 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
class operation:                #사칙연산 클래스 지정
    def sum(A,B):               # 덧셈 함수 생성
        print(A + B)

    def minus(A,B):             # 뺄셈 함수 생성
        print(A - B)
    
    def multiply(A,B):          # 곱셈 함수 생성
        print(A * B)

    def division(A,B):          # 나눗셈 함수 생성
        print(int(A/B))

    def remain(A,B):            # 나머지 함수 생성
        print(A%B)

A,B = map(int, input() .split())    #입력값을 변수 A,B로 지정

operation.sum(A,B)              #덧셈 출력
operation.minus(A,B)            #뺄셈 출력
operation.multiply(A,B)         #곱셈 출력
operation.division(A,B)         #나눗셈 출력
operation.remain(A,B)           #나머지 출력