# https://www.acmicpc.net/problem/17103
# 문제
## 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
## 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

# 입력
## 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

# 출력
## 각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

import sys
n = int(sys.stdin.readline().rstrip())

def question(n):
    input_list = [0]*n
    for i in range(n):
        input_list[i] = int(sys.stdin.readline().rstrip())
        pass
    repeat = max(input_list)
    answer_list = [1]*(repeat+1) 
    answer_list[0] = answer_list[1] = 0   
    for j in range(2,repeat+1):
        for k in range(j*j,repeat+1,j):
            answer_list[k] = 0
    for i in range(n):
        answer = 0
        for j in range(int(input_list[i]/2)+1):
            if answer_list[j] != 0 and answer_list[input_list[i] -j] != 0 :
                answer += 1
        print(answer)
    return 0

question(n)