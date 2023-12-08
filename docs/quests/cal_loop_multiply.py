# quest 
# - 사용자 입력 곱셈 계산기 
# - 'q'  입력 시 종료

def multiply(num_first,num_second) :  #곱셈 function 
    result = (num_first) * (num_second)
    return result

num_input = input() #입력값 작성
while num_input != "q":   
    list_a = list(map(int,num_input.split())) # 입력값 리스트로 변경
    num_first = list_a[0] # 입력값 숫자로 변경
    num_second = list_a[1]
    multiply(num_first,num_second)
    print(multiply(num_first,num_second))
    num_input = input() #입력값 다시 작성
pass #입력값이 q일 경우 종료.


# num_input = input() #입력값 작성
# while num_input != "q":   
#     list_a = list(map(int,num_input.split())) # 입력값 리스트로 변경
#     while True:
#         try:
#             num_first = list_a[0] # 입력값 숫자로 변경
#             num_second = list_a[1]
#             multiply(num_first,num_second)
#             print(multiply(num_first,num_second))
#             num_input = input() #입력값 다시 작성
#         except:
#             break

# pass #입력값이 q일 경우 종료.