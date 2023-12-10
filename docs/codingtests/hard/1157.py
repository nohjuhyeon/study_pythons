# https://www.acmicpc.net/problem/1157
# 문제
## 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력
## 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력
## 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

A = input().upper()
list_count= []
repeat = len(A)
check = 0
for i in range(repeat):
    count_same = 0
    for j in range(repeat):
        pass
        if A[i] == A[j]:
            count_same = count_same + 1
            pass
        else:
            pass
        pass
    list_count.append(count_same)
    pass
pass
print(max(list_count))
# for i in range(repeat):
#     if max(list_count) ==list_count[i]:
#         check = check + 1
#     else:
#         pass
# if check > 0:
#     print("?")
#     pass
# else:
#     print(max(list_count))
