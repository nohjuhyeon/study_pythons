# https://www.acmicpc.net/problem/2941
# 문제
## 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
## 크로아티아 알파벳	변경
## č	c=
## ć	c-
## dž	dz=
## đ	d-
## lj	lj
## nj	nj
## š	s=
## ž	z=
## 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
## dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
# 입력
## 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
## 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
# 출력
## 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

a = list(input())
for i in range(len(a)-2):
    if a[i] == "d" and a[i+1] == "z" and a[i+2] == "=":
        a[i] = 1
        a[i+1] = 2
        a[i+2] = 2
for i in range(len(a)-1):
    if a[i] == "c" and a[i+1] == "=":
        a[i] = 1
        a[i+1] = 2
        pass
    elif a[i] == "c" and a[i+1] == "-":
        a[i] = 1
        a[i+1] = 2
        pass
    elif a[i] == "d" and a[i+1] == "-":
        a[i] = 1
        a[i+1] = 2
    elif a[i] == "l" and a[i+1] == "j":
        a[i] = 1
        a[i+1] = 2
    elif a[i] == "n" and a[i+1] == "j":
        a[i] = 1
        a[i+1] = 2
    elif a[i] == "s" and a[i+1] == "=":
        a[i] = 1
        a[i+1] = 2
    elif a[i] == "z" and a[i+1] == "=":
        a[i] = 1
        a[i+1] = 2
    else:
        pass
for i in range(len(a)):
    if a[i] != 1 and a[i] != 2:
        if a[i] != "-" and a[i] != "=":
            a[i] = 1
print(a.count(1))

# a = list(input())
# if len(a) > 1:
#     for i in range(len(a)-1):
#         if a[i] == "c" and a[i+1] == "=":
#             a[i] = 1
#             a[i+1] = 2
#             pass
#         elif a[i] == "c" and a[i+1] == "-":
#             a[i] = 1
#             a[i+1] = 2
#         elif a[i] == "d" and a[i+1] == "z" and a[i+2] == "=":
#             a[i] = 1
#             a[i+1] = 2
#             a[i+2] = 2
#             pass
#         elif a[i] == "d" and a[i+1] == "-":
#             a[i] = 1
#             a[i+1] = 2
#         elif a[i] == "l" and a[i+1] == "j":
#             a[i] = 1
#             a[i+1] = 2
#         elif a[i] == "n" and a[i+1] == "j":
#             a[i] = 1
#             a[i+1] = 2
#         elif a[i] == "s" and a[i+1] == "=":
#             a[i] = 1
#             a[i+1] = 2
#         elif a[i] == "z" and a[i+1] == "=":
#             a[i] = 1
#             a[i+1] = 2
#         else:
#             pass
#     for i in range(len(a)):
#         if a[i] != 1 and a[i] != 2:
#             if a[i] != "-" and a[i] != "=":
#                 a[i] = 1
#     print(a.count(1))
# else:
#     for i in range(len(a)):
#         if a[i] != "-" and a[i] != "=":
#             a[i] = 1
#     print(a.count(1)) 
