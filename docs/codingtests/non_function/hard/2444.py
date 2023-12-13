# https://www.acmicpc.net/problem/2444
# 문제
## 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 입력
## 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
## 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

N = int(input())
repeat = (N * 2) - 1
# N = 1 - 1 1 
# N = 2 - 3 1 3 1
# N = 3 - 5 1 3 5 3 1 
# N = 4 - 7 1 3 5 7 5 3 1

for i in range(N):
    for j in range(N-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print("")
for i in range(N-1):
    for j in range(i+1):
        print(" ", end="")
    for j in range((2*N - 3) -2*i):
        print("*",end="")
    print("")

#          N =  (N/2)+1   /N( -1 + 2i)
#         N-1 =  i + 1  /   (2N -3) - 2i
#           N = 5 
#     *           4 1           
#    ***          3 3
#   *****         2 5
#  *******        1 7
# *********       0 9
#  *******        1 7
#   *****         2 5
#    ***          3 3
#     *           4 1

# 5 - 7 
# 4 - 5
# 3 - 3
# 2 - 1