## https://www.acmicpc.net/problem/2563
# 문제
## 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
## 예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.
# 입력
## 첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다
# 출력
## 첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.

# a = 3,7       3, 17   13, 7   13, 17
# b = 15, 7     15, 17  25, 7   25, 17
# c = 5,2       5, 12   15, 2   15, 12

# a_x = 3
# a_y = 7 
# b_x = 5
# b_y = 2

# if b_x >= a_x and b_x <= (a_x + 10) and b_y >= a_y and b_y <= (a_y + 10):
#     length_x = a_x+10 - b_x
#     length_y = a_y+10 - b_y
#     pass

# if (b_x + 10) >= a_x and (b_x + 10) <= (a_x + 10) and b_y >= a_y and b_y <= (a_y + 10):
#     length_x = b_x + 10 - a_x
#     length_y = a_y+ 10 - b_y
#     pass

# if b_x >= a_x and b_x <= (a_x + 10) and (b_y + 10) >= a_y and (b_y + 10) <= (a_y + 10):
#     length_x = a_x + 10 - b_x
#     length_y = b_y + 10 - a_y
#     pass

# if (b_x + 10) >= a_x and (b_x + 10) <= (a_x + 10) and (b_y + 10) >= a_y and (b_y + 10) <= (a_y + 10):
#     length_x = b_x + 10 - a_x
#     length_y = b_y + 10 - a_y
#     pass

# print(length_x * length_y)

# if a_x >= b_x and a_x <= (b_x + 10) and a_y >= b_y and a_y <= (b_y + 10):
#         pass
#     if (a_x + 10) >= b_x and (a_x + 10) <= (b_x + 10) and a_y >= b_y and a_y <= (b_y + 10):
#         pass
#     if a_x >= b_x and a_x <= (b_x + 10) and (a_y + 10) >= b_y and (a_y + 10) <= (b_y + 10):
#         pass
#     if (a_x + 10) >= b_x and (a_x + 10) <= (b_x + 10) and (a_y + 10) >= b_y and (a_y + 10) <= (b_y + 10):
#         pass

list_x = []
list_y = []
N = int(input())
for i in range(N):
    x,y = map(int,input().split())
    list_x.append(x)
    list_y.append(y)
print(list_x,list_y)
for i in range(N):
    for j in range(i,N):
        a_x = list_x[i]
        a_y = list_y[i]
        b_x = list_x[j]
        b_y = list_y[j]
        if b_x >= a_x and b_x <= (a_x + 10) and b_y >= a_y and b_y <= (a_y + 10):
            length_x = a_x+10 - b_x
            length_y = a_y+10 - b_y
            pass

        if (b_x + 10) >= a_x and (b_x + 10) <= (a_x + 10) and b_y >= a_y and b_y <= (a_y + 10):
            length_x = b_x + 10 - a_x
            length_y = a_y+ 10 - b_y
            pass

        if b_x >= a_x and b_x <= (a_x + 10) and (b_y + 10) >= a_y and (b_y + 10) <= (a_y + 10):
            length_x = a_x + 10 - b_x
            length_y = b_y + 10 - a_y
            pass

        if (b_x + 10) >= a_x and (b_x + 10) <= (a_x + 10) and (b_y + 10) >= a_y and (b_y + 10) <= (a_y + 10):
            length_x = b_x + 10 - a_x
            length_y = b_y + 10 - a_y
            pass
        print(length_x * length_y)