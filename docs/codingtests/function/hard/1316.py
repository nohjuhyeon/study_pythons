# https://www.acmicpc.net/problem/1316
# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

num_input = int(input())                        # 반복횟수 입력

def group_word_checker(num_input):
    num_checker = 0                            # 그룹 단어 카운트 변수 지정
    for i in range(num_input):
        str_input = input()                    # 문자 입력
        list_input = list(set(str_input))       
        check_num = 0                          # 체크 변수 지정
        for j in range(len(list_input)):
            str_count = str_input.count(list_input[j])      # 문자의 카운트 변수 지정
            str_index = str_input.index(list_input[j])      # 문자의 인덱스 변수 지정
            pass
            pass
            for k in range(str_index, str_index + str_count):
                if str_input[k] != str_input[str_index]:    # 그룹 단어가 아닐 경우
                    check_num += 1                          # 체크 변수 + 1
        if check_num == 0:                                  # 체크 변수가 0일 경우
            num_checker += 1                                # 카운트 변수 + 1
            pass
    print(num_checker)

group_word_checker(num_input)