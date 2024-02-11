bool_flag = True
pass
bool_flag = False
type(bool_flag)
# <class 'bool'>

# 문자 판단 
# 같음에 대한 기호는 ==
str_name = "juhyeon Noh"
str_name == "juhyeon Noh"
# True
str_name == "juhyeonNOh"
# False
# 다름에 대한 기호는 !=
str_name !="yojulab"
# True
str_name != "juhyeon Noh"
# False

# 숫자에 대한 판단 ( 변수 + 부등호 + 기준값)
# 컴퓨터 입장
# True = Yes = 1, False = No = 0
5 == 4
# False
num_first = 5
num_first == 4
# False
num_first != 4
# True
num_first > 4
# True
num_first >= 4
# True

# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B, 나머지 : F
my_score = 90
my_score >= 90
# True
my_score = 90
my_score >= 90
# True
my_score = 80
my_score > 80
# False

# 사람 말로 예, 아니오 판단 근거
# 정의는 정의하기 어렵다. -> 부정(아니오)
# 정의는 정의하기 어렵지 아니하다. -> 긍정(예)
# 50점 이상부터 60점 이하는 c 학점이다. -> 대상이 없어 판단 어려움.

# 컴퓨터는 상태를 확인할 떄 논리 연산자(True, False) 사용
# 현재 값이 75점 이상부터 85점 이하는 C 학점이다.
# 75 ~ 85점 -> and 조건
my_score >= 75
# True
my_score <= 85
my_score >= 75 and my_score <= 85
# True

# 논리(True or False) 연산자(결과값)
# and : 1 and 1 -> 1, 나머지는 0
# or : ~도 되고, 
# not : 반대로 변환

# 부등호 사용 시 결과는 True or False(boolean)
# 논리 연산자(True or False 대한 결과값)
first = 200
second = 33 
third = 500
if first > second and third > first : 
    print("Both conditions are True")
pass

print("End Program") 
pass


