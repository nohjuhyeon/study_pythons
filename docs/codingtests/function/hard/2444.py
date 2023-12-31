# # https://www.acmicpc.net/problem/2444
# # 문제
# ## 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# # 입력
# ## 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# # 출력
# ## 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

#     *             4 1
#    ***            3 3
#   *****           2 5
#  *******          1 7
# *********         0 9
#  *******          1 7
#   *****           2 5
#    ***            3 3
#     *             4 1

length_input = int(input())

def star(length_input):
    for i in range(length_input):                   # 별의 개수가 올라가는 동안 반복
        for j in range(length_input-i - 1):         # 빈칸이 하나씩 감소
            print(" ",end="")                       
        for j in range(2*i + 1):
            print("*",end="")                       # 별이 2개씩 증가
        print("")
    for i in range(length_input - 1):              # 별의 개수가 내려가는 동안 증가
        for j in range(i + 1):
            print(" ",end="")                      # 빈칸 하나씩 증가
        for j in range(2*(length_input-2)+ 1- 2*i):
            print("*",end="")                      # 별의 개수가 2개씩 감소
        print("")

star(length_input)