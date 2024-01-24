# https://www.acmicpc.net/problem/3009
# 문제
## 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 입력
## 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
# 출력
## 직사각형의 네 번째 점의 좌표를 출력한다.

def question():
    list_A = []
    list_B = []
    answer_A = []
    answer_B=[]
    for i in range(3):
        A,B = map(int,input().split())
        list_A.append(A)
        list_B.append(B)
    set_A = list(set(list_A))
    set_B = list(set(list_B))
    for i in range(len(set_A)):
        if list_B.count(set_B[i]) == 1:
            answer_B = set_B[i]
        if list_A.count(set_A[i]) == 1:
            answer_A = set_A[i]
    answer = [answer_A,answer_B]
    return answer
answer = question()
print(*answer)