# https://www.acmicpc.net/problem/5597
# 문제
## X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
## 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.
# 입력
## 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
# 출력
## 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

class quest:
    def __init__(self):
        self.list_student = []                                                      # 학생들 리스트 변수 지정
        for i in range(28):                                                         # 28번 반복
            self.num_student = int(input())                                         # 학생 출석 변호 입력
            self.list_student.append(self.num_student)                              # 입력 받은 출석 변호 리스트에 추가
    def find_student(self):
        for i in range(30):                                                         # 1-30번까지 비교
            check_list = 0                                                          # 체크하는 변수 지정
            for j in range(len(self.list_student)):                                 # 출석 번호 리스트 만큼 반복
                if self.list_student[j] == i+1:                                     # 출석 변호와 1-30 숫자 비교
                    check_list += 1                                                 # 있을 시 체크하는 변수 +1
                    pass
            pass
            if check_list != 1:                                                     # 체크 리스트가 1이 아닐 경우 프린트
                print(i+1)


Quest= quest()
Quest.find_student()