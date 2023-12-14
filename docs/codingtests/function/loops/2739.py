# https://www.acmicpc.net/problem/2739
# 문제
## N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

# 입력
## 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.

# 출력
## 출력형식과 같게 N*1부터 N*9까지 출력한다.

class quest():
    def __init__(self):
        self.num_input = int(input())                                           #출력한 구구단의 단수 입력
    
    def multifly(self,num_i):
        num_multifly = self.num_input * num_i                                  # 곱셈을 진행하는 함수 작성
        return num_multifly
    pass

    def Print(self,num_multifly,num_i):
            print("{} * {} = {}".format(self.num_input,num_i,num_multifly))     # 곱셈의 과정과 결과를 출력하는 함수 작성
            pass
    pass

Quest = quest()
for i in range(9):                                                              # 1-9까지의 곱셈 진행 및 출력
    num_i = i + 1
    multifly_output = Quest.multifly(num_i)
    Quest.Print(multifly_output,num_i)

