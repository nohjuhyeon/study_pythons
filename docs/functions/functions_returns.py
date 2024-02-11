## call by value
## 나오는 값 처리
# first = 5
# second = 4
# sum = first + second
def add ():
    first = 5
    second = 4
    sum = first + second
    # return 0
    return sum # 상수 대신 변수 사용


# num_sum = 0
num_sum = add()
print("add의 return 결과 : {}".format(num_sum))

# num_first = 4
# num_second = 5
# # 곱셈 연산
# num_first * num_second

#두 수를 곱해서 나오는 기능
def multiply() :
    num_first = 4
    num_second = 5
    # 곱셈 연산
    result = num_first * num_second
    return result

num_multiply = multiply()
print("num_multiply return value : {}".format(num_multiply))


# list_fruits = ["melon","apple", "banana", "cherry"]
# ## index로 값 가져오기
# list_fruits[0] # 단일 변수로 여김 1차원(행)
def return_list() : 
    list_fruits = ["melon","apple", "banana", "cherry"]
    return list_fruits

print("retrun_list() retrun result : {}".format(return_list()))


def return_listbyindex() : 
    list_fruits = ["melon","apple", "banana", "cherry"]
    ## index로 값 가져오기
    list_fruits[0] # 단일 변수로 여김 1차원(행)
    return list_fruits[0]

print("return_listbyindex() retrun result : {}".format(return_listbyindex()))

# my_score = 79
# if my_score >= 90 : #90점 이상 : A 
#     pass
#     print("{}은 90점 이상으로 A학점".format(my_score))
# elif my_score > 80 : # 80점 초과 : B
#     pass
#     print("{}은 80점 초과므로 B학점".format(my_score))
# else :  # 나머지 : F
#     pass
#     print("{}은 80점 이하이므로 F학점".format(my_score))
# 반복 print 작업 줄이기 위한 function 만들기 
def return_grade() : 
    my_score = 79
    if my_score >= 90 : #90점 이상 : A 
        my_grade = 'A'
        pass
    elif my_score > 80 : # 80점 초과 : B
        my_grade = 'B'
        pass
    else :  # 나머지 : F
        my_grade = 'C'
        pass
    # return_listbyindex() function 내에서도 호출이 가능함 
    return my_grade

str_grade = return_grade()
print("당신의 학점 : {}.".format(str_grade))
