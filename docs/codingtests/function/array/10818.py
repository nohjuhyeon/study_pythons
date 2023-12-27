# https://www.acmicpc.net/problem/10818
# 문제
## N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
# 출력
## 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

class quest:
    def __init__(self,repeat,check):
        self.num_repeat = repeat                                            # 반복 횟수 입력
        self.list_check = check                                             # 리스트 지정
    def max_min(self):
        list_print = [min(self.list_check),max(self.list_check)]            # 최소값, 최대값 지정
        print(*list_print)                                                  # 리스트 출력

repeat = int(input())
check = list(map(int,input().split()))

Quest = quest(repeat,check)
Quest.max_min()