# 문제 설명
## 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.
# 제한 조건
## strings는 길이 1 이상, 50이하인 배열입니다.
## strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
## strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
## 모든 strings의 원소의 길이는 n보다 큽니다.
## 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
# 입출력 예
## strings	n	return
## ["sun", "bed", "car"]	1	["car", "bed", "sun"]
## ["abce", "abcd", "cdx"]	2	["abcd", "abce", "cdx"]
# 입출력 예 설명
# 입출력 예 1
## "sun", "bed", "car"의 1번째 인덱스 값은 각각 "u", "e", "a" 입니다. 이를 기준으로 strings를 정렬하면 ["car", "bed", "sun"] 입니다.
# 입출력 예 2
## "abce"와 "abcd", "cdx"의 2번째 인덱스 값은 "c", "c", "x"입니다. 따라서 정렬 후에는 "cdx"가 가장 뒤에 위치합니다. "abce"와 "abcd"는 사전순으로 정렬하면 "abcd"가 우선하므로, 답은 ["abcd", "abce", "cdx"] 입니다.



def solution(strings, n):
    list_number = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]   
    list_num = []
    list_check = []
    answer = []
    for i in range(len(strings)):
        str_index = ""
        for j in range(len(strings[i])):
            if list_number.index(strings[i][j]) < 10 : 
                str_index += "0"
            str_index += str(list_number.index(strings[i][j]))
        list_num.append(str_index)
    for i in range(len(list_num)):
        if int(list_num[i][2*n]+list_num[i][2*n+1]) not in list_check:
            list_check.append(int(list_num[i][2*n]+list_num[i][2*n+1]))
    list_check = sorted(list_check)
    for i in range(len(list_check)):
        list_index_check = []
        for j in range(len(list_num)):
            if int(list_num[j][2*n]+list_num[j][2*n+1]) == list_check[i]:
                list_index_check.append(list_num[j])
        list_index_check = sorted(list_index_check)
        for j in range(len(list_index_check)):
            answer.append(strings[list_num.index(list_index_check[j])])
    return answer

strings = ["sun", "bed", "car"]
n = 1
answer = solution(strings,n)
print(answer)