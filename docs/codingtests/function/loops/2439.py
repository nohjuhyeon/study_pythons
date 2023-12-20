# https://www.acmicpc.net/problem/2439
# 문제
## 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
## 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
# 입력
## 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
## 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

class quest:
    def __init__(self):
        self.num_input = int(input())                              # 반복 횟수 입력 
    def star(self):
        list_star = []
        for i in range(self.num_input):                           # 반복 횟수 만큼 출력
                list_star.append(" ")                             # 공백으로 구성되어 있는 리스트 작성
        for i in range(self.num_input):
            list_star[self.num_input - i - 1] = "*"               # 반복 될 떄마다 뒤에서부터 "*"추가 
            for j in range(len(list_star)):                       # 리스트 출력
                  print(list_star[j],end=(""))
                  pass
            print("")
            
Quest = quest()
Quest.star()