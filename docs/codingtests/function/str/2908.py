# https://www.acmicpc.net/problem/2908
# 문제
## 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
## 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
## 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
# 출력
## 첫째 줄에 상수의 대답을 출력한다.

str_list = input().split()

def max_reverse(str_list):
    for i in range(len(str_list[0])):                           # 문자열의 길이만큼 반복
        if int(str_list[0][-i-1]) > int(str_list[1][-i-1]):     # 마지막 숫자부터 크기 비교
            for j in range(len(str_list[0])):                   # 역순으로 프린트
                print(str_list[0][-j-1],end="")
            break
        elif int(str_list[0][-i-1]) < int(str_list[1][-i-1]):
            for j in range(len(str_list[1])):
                print(str_list[1][-j-1],end="")
            break
        else: 
            pass
max_reverse(str_list)