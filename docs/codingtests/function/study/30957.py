# 문제
## 서울사이버대학교 빅데이터·정보보호학과는 빅데이터에 관심이 있는 학생들과 정보보호에 관심이 있는 학생들이 골고루 섞여 있는 학과이다. 2024학년도를 맞이하여 서울사이버대학교는 인공지능학과를 새로 만들게 되었다.
## 빅데이터·정보보호학과와 인공지능학과의 교육과정을 함께 구상하던 노교수와 천교수는 학생들이 빅데이터, 정보보호, 인공지능 중 어느 분야에 더 관심이 많은지 궁금해졌다. 그래서 학생들을 만날 때마다 항상 이를 물어보고 답을 B, S, A로 구분하여 메모장에 적어두었다. (B는 빅데이터, S는 정보보호, A는 인공지능을 의미한다.)
## 지금 상태로는 한눈에 들어오지 않아 학생들이 빅데이터, 정보보호, 인공지능 중 어느 분야에 더 관심이 많은지를 알아내기 어렵기 때문에, 당신에게 분석을 의뢰했다. 물어본 학생의 수와 답이 주어질 때, 결과를 출력하자.
# 입력
## 첫 번째 줄에 물어본 학생의 수 N이 주어진다. (1 <= N  <= 10^5) 
## 두 번째 줄에 메모장에 적힌 답들이 한 줄의 문자열로 주어진다. 문자열은 B, S, A로만 구성되어 있다.
# 출력
## 첫 번째 줄에 가장 많은 학생의 관심을 받는 분야의 문자를 출력한다. 만약 가장 많은 학생의 관심을 받는 분야가 2개라면, B, S, A의 순서로 모두 출력한다. 만약 세 분야의 관심이 동일하면, SCU를 출력한다. (SCU는 Seoul Cyber University의 약자이다.)

class quest:
    def __init__(self):
        self.num_len = int(input())
        self.str_input = input()
        self.list_count = []
        self.list_print = []
        self.list_len = []
    def max(self):
        for i in range(self.num_len):
            self.list_len.append(self.str_input[i])
        set_len = set(self.str_input)
        set_len = list(set_len)
        pass
        for i in range(len(set_len)):
            self.num_count = self.list_len.count(set_len[i])
            self.list_count.append(self.num_count)
        num_max_count = max(self.list_count)
        for i in range(len(self.list_count)):
            if self.list_count[i] == num_max_count:
                self.list_print.append(set_len[i])
        pass
        if len(self.list_print) == len(self.list_count):
            print("SCU")
        else:
            for i in range(len(self.list_print)):
                print(self.list_print[i], end="")
        

Quest = quest()
Quest.max()

        