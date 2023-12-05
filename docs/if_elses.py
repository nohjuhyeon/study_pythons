# 기본 if - elif - else 구문
if True:
    pass
elif True : 
    pass
else :
    pass

#문자 비교
str_name = "juhyeon Noh"

# 질문 형식(condition) = 변수 + 부등호 + 기준값  
# 문자에 대한 긍정으로 질문
if str_name == "juhyeon Noh":
    pass
    print("name is {}." .format(str_name))

# 문자에 대한 부정으로 질문
if str_name != "juhyeon Noh":
    pass
    print("name is not {}." .format(str_name))

print("End Program!")