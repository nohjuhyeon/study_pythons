# https://www.acmicpc.net/problem/10950
# 문제
## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
## 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력
## 각 테스트 케이스마다 A+B를 출력한다.

class quest():
    def __init__(self):
        self.num_repeat = int(input())                              # 반복횟수 입력

        pass

    def sum(self):
        num_sumA,num_sumB = map(int,input().split())                # 더할 값 입력
        num_sum = num_sumA + num_sumB                               # 입력 받은 값끼리 덧셈
        return num_sum
    


Quest = quest()
for i in range(Quest.num_repeat):                                  #반복횟수 만큼 덧셈 진행
    sum_input = Quest.sum()
    print(sum_input)