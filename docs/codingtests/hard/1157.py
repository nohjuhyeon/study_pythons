# https://www.acmicpc.net/problem/1157
# 문제
## 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력
## 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력
## 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# A = input().upper()
# list_count= []
# repeat = len(A)
# check = 1
# list_max=[]
# for i in range(repeat):
#     count_same = 0
#     for j in range(repeat):
#         pass
#         if A[i] == A[j]:
#             count_same = count_same + 1
#             pass
#         else:
#             pass
#         pass
#     list_count.append(count_same)
#     pass
# pass
# print(max(list_count))
# print(list_count)
# for i in range(len(list_count)):
#     if list_count[i] == max(list_count):
#         list_max.append(i)
#         pass
#     pass
# print(list_max)
# for i in range(len(list_max)):
#     for j in range(len(list_max)):
#         if A[list_max[i]] != A[list_max[j]]:
#             check = check * 0
#             pass
#         pass
#     pass
# print(check)
# if check == 1:
#     print(A[list_max[0]])
#     pass
# else:
#     print("?")

# A =input().upper()
# count_list = []
# for i in range(len(A)): 
#     count_list.append(A.count(A[i]))
#     pass
# print(count_list)
# pass
# if max(count_list) == count_list.count(max(count_list)):
#     print(A[count_list.index(max(count_list))])
#     pass
# else: 
#     print("?")


# A = input().upper()
# B = A.count(A[0])
# C = 0
# for i in range(len(A)):
#     if A.count(A[i]) >= B:
#         B = A.count(A[i])
#         D= A[i]
# for i in range(len(A)):
#     if B == A.count(A[i]):
#         C = C + 1
# if B == C:
#     print(D)
#     pass
# else:
#     print("?")

A = input().upper()
list_A=[]
list_B=[]
C = 1
for i in range(len(A)):
    list_A.append(A.count(A[i]))
for i in range(len(list_A)):
    if list_A[i] == max(list_A):
        list_B.append(A[i])
for i in range(len(list_B)):
    if list_B[i] != list_B[0]:
        C = 0
    else:
        pass
if C == 1:
    print(list_B[0])
else:
    print("?")