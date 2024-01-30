# https://www.acmicpc.net/problem/2751
# 문제
## N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
## 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
## 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# n = int(input())

# def question(n):
#     answer= []
#     a = 1
#     for i in range(n):
#         answer.append(int(input()))
#     while True:
#         if a in answer:
#             for i in range(answer.count(a)):
#                 print(a)
#         a += 1
#         if a > max(answer):
#             break
#     return 0

# question(n)
    
# n = int(input())

# def question(n):
#     answer= {}
#     for i in range(n):
#         answer[i] = int(input())
#     answer_array = sorted(answer.items(), key = lambda x:x[1])
#     for i in range(len(answer_array)):
#         print(answer_array[i][1])
#     return 0

# question(n)
    
# n = int(input())

# def question(n):
#     answer= {}
#     for i in range(n):
#         answer_element = input()
#         answer[answer_element] = answer_element
#     answer_array = sorted(answer)
#     for i in range(len(answer_array)):
#         print(answer_array[i])
#     return 0

# question(n)
import sys      

n = int(sys.stdin.readline())

def question(n):
    answer = [0]*n
    for i in range(n):
        answer[i]= int(sys.stdin.readline())
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
    return 0

question(n)
    