# https://www.acmicpc.net/problem/2438
# 문제
## 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 입력
## 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
## 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

class quest:
    def __init__(self):
        self.num_input = int(input())                                          # 반복 횟수 입력
    def star(self):
        for i in range(self.num_input):                                       # 반복 횟수만큼 반복 출력
            for j in range(i+1):                                              # 줄이 추가 될때마다 별의 개수 증가
                print("*",end="")
            print("")

Quest = quest()
Quest.star()