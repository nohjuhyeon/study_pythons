# https://www.acmicpc.net/problem/1316
# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.
N = int(input())
output = 0
for i in range(N):
    str_word = list(input())
    alphabet_list = list(set(str_word))
    check = 1
    for j in range(len(alphabet_list)):
        alphabet_count = str_word.count(alphabet_list[j])
        alphabet_index = str_word.index(alphabet_list[j])
        for k in range(alphabet_count):
            if str_word[alphabet_index] == str_word[alphabet_index + k]:
                check = check * 1
                pass
            else:
                check = 0
    if check == 1:
        output = output + 1
        pass
print(output)

    