# https://www.acmicpc.net/problem/2562
# 문제
## 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
## 예를 들어, 서로 다른 9개의 자연수
## 3, 29, 38, 12, 57, 74, 40, 85, 61
## 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
# 입력
## 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 출력
## 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.


class quest:
    def __init__(self):
        self.num_input = int(input())                                   # 반복횟수 입력
        self.list_input = list(input().split())                         # list 입력
        self.num_check = input()                                        # 찾을 번호 입력
        self.num_count = 0                                              # 카운트 기본값 설정
    def count(self):
        for i in range(self.num_input):                                 # 반복횟수만큼 반복
            if self.num_check == self.list_input[i]:                    # 찾을 번호가 list에 들어 있는 번호와 동일할 경우
                self.num_count += 1                                     # 카운트 + 1
        print(self.num_count)

Quest = quest()
Quest.count()