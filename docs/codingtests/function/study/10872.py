# https://www.acmicpc.net/problem/10872
# 문제
## 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
# 출력
## 첫째 줄에 N!을 출력한다.

class quest:
    def __init__(self):
        self.num_input = int(input())                                       # 정수 입력
    def factorial(self):
        num_factorial = 1                                                   # num_factorial을 기본 값(1)으로 설정
        for i in range(self.num_input):                                     # num_input만큼 반복
            num_factorial = num_factorial * (i + 1)                         # num_factorial를 1부터 num_input까지 순서대로 곱셈
        return num_factorial                                                # 곱셈 결과 return
Quest = quest()                                                             # class에 연결하는 변수 설정
print(Quest.factorial())                                                    # 곱셈 결과 출력 