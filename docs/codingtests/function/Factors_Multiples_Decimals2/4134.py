# https://www.acmicpc.net/problem/4134
# 문제
## 정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

# 입력
## 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

# 출력
## 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

import sys

n = int(sys.stdin.readline().rstrip())

def question(n):
    for i in range(n):
        answer_num = int(sys.stdin.readline().rstrip())
        if  answer_num <= 2:
            print(2)
        else:
            answer = 0
            while True:
                repeat = int((answer_num**(0.5)))+1
                for i in range(2,repeat+1):
                    if answer_num%(i) == 0:
                        answer = 0
                        break
                    else:
                        answer = answer_num
                if answer != 0:
                    break
                else:
                    answer_num += 1
            print(answer)
    return 0

question(n)

# answer_list = [True]*4000000001
# answer_list[0]=answer_list[1]=False
# for i in range(2,int(4000000000**0.5)+1):
#     if answer_list[i]==True:
#         for j in range(i*i,4000000001,i):
#             answer_list[j] == False
# print(n,answer_list)    
