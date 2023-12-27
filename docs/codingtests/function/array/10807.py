# https://www.acmicpc.net/problem/10807
# 문제
## 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
# 출력
## 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

class quest:
    def __init__(self):
        self.num_input= int(input())                            # 반복 횟수 입력
        self.list_num = list(map(int,input().split()))          # 비교할 리스트 입력
        self.num_check = int(input())                           # 비교값 입력
        self.num_count = 0                                      # 카운트 기본값 설정
    def count_num(self):
        for i in range(self.num_input):                         # 입력한 반복 횟수만큼 반복
            if self.num_check == self.list_num[i]:              # 만약에 리스트와 비교값이 같을 경우
                self.num_count += 1                             # 카운트 + 1
        print(self.num_count)

Quest = quest()
Quest.count_num()