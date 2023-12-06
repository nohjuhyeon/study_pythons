# for 기본 문형
for x in []:
    pass

# 얼마만큼 반복할지에 대한 값들을 알려줌
numeric = 0
numerics = [0, 1, 2, 3, 4] # 5개수 값으로 이루어진 리스트
for number in numerics:
    pass
    print(number)

# 문자 3개 값들로 이루어진 리스트
for x in ["apple", "banana", "cherry"]:
    pass
    print("fruit name : {}!".format(x))

list_fruits = ["apple", "banana", "cherry"]
for str_fruit in list_fruits:
    pass
    print("fruit name : {}!" .format(str_fruit))
print("End program!")

numerics = [0, 1, 2, 3, 4] # 5개수 값으로 이루어진 리스트
for number in numerics:
    pass
    # print("Number : {}." .format(number))
    print("Number : {}." .format(number+2))
print("End program!")
