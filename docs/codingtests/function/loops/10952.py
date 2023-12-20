# https://www.acmicpc.net/problem/10952
# 문제
## 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력
## 입력은 여러 개의 테스트 케이스로 이루어져 있다.
## 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
## 입력의 마지막에는 0 두 개가 들어온다.
# 출력
## 각 테스트 케이스마다 A+B를 출력한다.

    
def sum():
   while True:                                              # break 될 때까지 반복문 진행
      num_A,num_B = map(int, input().split())               # num_A, num_B 입력
      if num_A == 0 and num_B == 0:                         # num_A와 num_B가 모두 0일 경우 break
         break
      else:                                                 # 아닐 경우 num_A + num_B 출력
          print(num_A + num_B)

sum()