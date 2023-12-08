# https://www.acmicpc.net/problem/2439
# 문제
## 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
## 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
# 입력
## 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
## 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.



A = int(input())
b = 0

for a in range(A):
    b = b + 1
    a = A - b
    x = 0
    y = 0
    c = ""
    d = ""
    while x < b:
        x =x + 1
        c = "*{}".format(c)
        pass
    while y < a:
        y = y + 1
        d = " {}".format(d)
        pass    
    print("{}{}".format(d,c))

    