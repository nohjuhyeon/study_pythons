# https://www.acmicpc.net/problem/11720
# 문제
## N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
# 출력
## 입력으로 주어진 숫자 N개의 합을 출력한다.

def sum_num(num_repeat,num_list):
    sum_list = 0                                    # list의 합 변수 지정
    for i in range(num_repeat):                     # 반복횟수 만큼 반복
        sum_list = sum_list + int(num_list[i])      # list 내에 있는 값들을 더함
    return sum_list

num_repeat = int(input())
num_list = list(input())

sum_list = sum_num(num_repeat,num_list)
print(sum_list)