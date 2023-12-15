# https://www.acmicpc.net/problem/11021
# 문제
## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
## 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
## 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

import sys                                                                                      # sys 실행

class quest():
    def __init__(self):
        self.A = int(input())                                                                  # 입력한 반복횟수 self.A로 지정
        self.E = 0                                                                             # self.E는 0으로 지정
    def sum(self):
        for D in range(self.A):                                                                # self.A 만큼 반복
            B, C = map(int, sys.stdin.readline() .split())                                     # 더할 값 두 개 입력
            self.E = self.E + 1                                                                # 답안 번호 지정
            D = B + C 
            print("Case #{}: {} ".format(self.E,D))

Quest = quest()
Quest.sum()