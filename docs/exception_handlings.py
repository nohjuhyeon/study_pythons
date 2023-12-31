# 기본 구문
try:
    pass    # 업무 코드
except:
    pass    # 업무 코드 문제 발생 시 대처 코드 
finally:
    pass    # try 나 except이 끝난 후 무조건 실행 코드 



# pure python with 계산기

num_first = '4'
num_second = 5
# 곱셈 연상

try:
    result = num_first / num_second
    pass    # 업무 코드
except:
    result = int(num_first) / int(num_second)
    pass    # 업무 코드 문제 발생 시 대처 코드 
finally:
    pass    # try 나 except이 끝난 후 무조건 실행 코드 

print("{} = {} * {}".format(result, num_first,num_second))
pass

# function in try exception

def function_name():
    try:
        result = num_first / num_second
        pass    # 업무 코드
    except:
        result = int(num_first) / int(num_second)
        pass    # 업무 코드 문제 발생 시 대처 코드 
    finally:
        pass    # try 나 except이 끝난 후 무조건 실행 코드 
    pass                # 내용 넣기
    return 0