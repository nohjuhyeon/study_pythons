# https://www.acmicpc.net/problem/10872
# 문제
## 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
# 출력
## 첫째 줄에 N!을 출력한다.

## 알고리즘 작성
# 1. 계산할 값(N) 입력 
# 2. for 문을 시작하기 전에 기본값(1)을 설정
# 3. 1부터 N까지 계속 곱하는 반복문 필요    -> for i in range(N):
# 4. 반복문이 진행될수록 곱할 값은 1이 증가
# 5. 곱셈 진행
# 6. 결과값 출력


## 1번째 방법
num_repeat = int(input())                                       # 1. 계산할 값(N) 입력
a = 0                                       
b = 1                                                           # 2. for 문을 시작하기 전에 기본값(1)을 설정
for i in range(num_repeat):                                     # 3. 1부터 N까지 계속 곱하는 반복문 필요    -> for i in range(num_repeat):
    a = a + 1                                                   # 4. 반복문이 진행될수록 곱할 값은 1이 증가
    b = b*a                                                     # 5. 곱셈 진행
    pass
print(b)                                                        # 6. 결과값 출력

## 2번째 방법
# num_input = int(input())                                                   # 1. 계산할 값(N) 입력
# num_factorial = 1                                                          # 2. for 문을 시작하기 전에 기본값(1)을 설정
# for i in range(num_input):                                                 # 3. 1부터 N까지 계속 곱하는 반복문 필요    -> for i in range(num_input):
#     num_factorial = num_factorial * (i + 1)                                # 4. 반복문이 진행될수록 곱할 값은 1이 증가: i + 1       # 5. 곱셈 진행
#     pass
# print(num_factorial)                                                       # 6. 결과값 출력


## 3번째 방법
# class quest:
#     def __init__(self):                                                     # class 내에서 사용할 변수 지정
#         self.num_input = int(input())                                       # 1. 계산할 값(N) 입력
#     def factorial(self):                                                    # 계산하는 함수 작성
#         num_factorial = 1                                                   # 2. for 문을 시작하기 전에 기본값(1)을 설정
#         for i in range(self.num_input):                                     # 3. 1부터 N까지 계속 곱하는 반복문 필요    -> for i in range(num_input):
#             num_factorial = num_factorial * (i + 1)                         # 4. 반복문이 진행될수록 곱할 값은 1이 증가: i + 1       # 5. 곱셈 진행 
#             pass
#         return num_factorial                                                # 결과값 return
# Quest = quest()                                                             
# print(Quest.factorial())                                                    # 6. 결과값 출력

