# https://www.acmicpc.net/problem/25206
# 문제
## 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!
## 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
## 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
## 인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.
## A+	4.5
## A0	4.0
## B+	3.5
## B0	3.0
## C+	2.5
## C0	2.0
## D+	1.5
## D0	1.0
## F	0.0
## P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
## 과연 치훈이는 무사히 졸업할 수 있을까?
# 입력
## 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
# 출력
## 치훈이의 전공평점을 출력한다.
## 정답과의 절대오차 또는 상대오차가 (10^{-4}) 이하이면 정답으로 인정한다.
# 제한
## 1 ≤ 과목명의 길이 ≤ 50
## 과목명은 알파벳 대소문자 또는 숫자로만 이루어져 있으며, 띄어쓰기 없이 주어진다. 입력으로 주어지는 모든 과목명은 서로 다르다.
## 학점은 1.0,2.0,3.0,4.0중 하나이다.
## 등급은 A+,A0,B+,B0,C+,C0,D+,D0,F,P중 하나이다.
## 적어도 한 과목은 등급이 P가 아님이 보장된다.
def class_list():
    list_class = []
    list_score =[]
    for i in range(20):
        class_input = input().split()
        if class_input[2] != "P":                   # P를 제외한 전공평점을 숫자로 변경
            if class_input[2] == "A+":
                class_input[2] = 4.5
            elif class_input[2] =="A0":
                class_input[2] = 4.0
            elif class_input[2] =="B+":
                class_input[2] = 3.5
            elif class_input[2] =="B0":
                class_input[2] = 3.0
            elif class_input[2] =="C+":
                class_input[2] = 2.5
            elif class_input[2] =="C0":
                class_input[2] = 2.0
            elif class_input[2] =="D+":
                class_input[2] = 1.5
            elif class_input[2] =="D0":
                class_input[2] = 1.0
            elif class_input[2] == "F":
                class_input[2] = 0.0
            list_score.append(class_input[2])
            list_class.append(float(class_input[1]))        # 문자들을 숫자화
        pass
    return list_class,list_score

def calculator(list_class,list_score):
    list_sum = []
    for i in range(len(list_class)):
        list_sum.append(list_class[i]*list_score[i])       
    num_sum = sum(list_sum)/sum(list_class)                 # 평점 평균 구하기
    pass
    return num_sum

list_class,list_score = class_list()
num_sum = calculator(list_class,list_score)
print(num_sum)