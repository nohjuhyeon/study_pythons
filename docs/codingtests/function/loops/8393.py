# https://www.acmicpc.net/problem/8393
# 문제
## n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 출력
## 1부터 n까지 합을 출력한다.


class quest():
    def __init__(self):
        self.repeat = int(input())

    def sum(self):
        sum = 0
        for i in range(self.repeat):
            num_i = i + 1
            sum = sum + num_i
        return sum
    

Quest = quest()

print(Quest.sum())

