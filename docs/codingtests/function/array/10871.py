# https://www.acmicpc.net/problem/10871
# 문제
## 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
## 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
# 출력
## X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

class quest:
    def __init__(self):
        self.num_A,self.num_B = map(int,input().split())            # 반복 횟수와, 비교 값 입력
        self.list_num = list(map(int,input().split()))              # 비교할 리스트 입력
        self.print_list = []                                        # 출력할 리스트 변수 설정
    def check_small(self):
        for i in range(self.num_A):                                 # 반복횟수만큼 반복
            if self.list_num[i] < self.num_B:                       # 비교 값보다 작을 경우
                self.print_list.append(self.list_num[i])            # 출력할 리스트에 추가
        print(*self.print_list)

Quest =quest()
Quest.check_small()