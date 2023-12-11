class Arithmetics:
    def minus(self, first,second) :
        result = first - second
        return result    
    
    def multiply(self, first, second) : # 호출 시 변수에 값이 할당 됨
        result = first * second 
        pass
        return result # 상수 대신 변수 사용
    
    def division(self, first, second) : # 호출 시 변수에 값이 할당 됨
        result = first / second 
        pass
        return result # 상수 대신 변수 사용

input_list = list(input().split()) # 계산할 두 값 입력
if len(input_list) == 2: 
    try:    
        num_A = int(input_list[0])
        num_B = int(input_list[1])
        if num_B == 0:
            print("자연수를 입력하세요")
        else:
            arithmetics = Arithmetics() # 생성자 호출
            print("뺼셈 : {}".format(arithmetics.minus(num_A,num_B))) # 원하는 기능 호출/뺄셈 결과값 호출
            print("곱셈 : {}".format(arithmetics.multiply(num_A,num_B))) # 원하는 기능 호출/곱셈 결과값 호출
            print("나눗셈 : {}".format(arithmetics.division(num_A,num_B))) # 원하는 기능 호출/나눗셈 결과값 호출
    except:
        print("숫자를 입력하세요.")
        pass
else:
    print("값을 두 개를 입력하세요.")  

