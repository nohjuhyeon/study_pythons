numberic_first = 0
numberic_second = 1
numberic_third = 2
numberic_fourth = 3
numberic_fifth = 4
numerics = [0, 1, 2, 3, 4]  # 5개수 값으로 이루어진 리스트

# 사용 이유: 값들에 모임을 쉽게 전달
# 숫자 5개 값들로 이루어진 리스트
list_numerics = [0, 1, 2, 3, 4]
# 문자 3개 값들로 이루어진 리스트
list_fruits = ["apple", "banana", "cherry"]
# 숫자와 문자 섞은 리스트 -> 가능은 하지만 우린 쓰지 않는다
list_mixs = [0, 1, 2, 3, "apple", "banana"]

len(list_numerics)
# 5
len(list_mixs)
# 6

## for 문 활용 후 다시 오기
list_fruits = ["melon","apple", "banana", "cherry"]
## index로 값 가져오기
list_fruits[0] # 단일 변수로 여김 1차원(행)
# 'melon'
list_fruits[3]
# 'cherry'
# 에러 발생
# list_fruits[4]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# IndexError: list index out of range
pass

# 설문 답변 받기

# 1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?           index 0
# A. Windows B. macOS C. Linux D. Chrome OS E. 기타     index 1
# 당신의 답변 : A
# 2. 주로 사용하는 프로그래밍 언어는 무엇인가요?           index 2
# A. Python B. Java C. JavaScript D. C++ E. 기타        index 3
# 당신의 답변 : D
# 3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?     index 4
# A. Python B. Java C. JavaScript D. C++ E. 기타        index 5
# 당신의 답변 : E

list_polls = ["1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
              ,"A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
              ,"2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
              ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
              ,"3. 개발자에게 인기 있는 프로그래밍 언어는 무엇인가요?"
              ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
              ]

for num_count in [0,2,4]:
    str_content =list_polls[num_count]
    print("{}".format(str_content))
    print("------------------------")
    pass
print("End program!")

#list 초기화 방식
list_fruits_primitive = ["melon", "apple", "banana", "cherry"]
tuple_fruits = ("melon", "apple", "banana", "cherry")                       #튜플은 내용을 변경할 수 없음 
list_fruits_constructor = list(("melon", "apple", "banana", "cherry"))

pass