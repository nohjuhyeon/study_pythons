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

num_A,num_B = map(int, input().split()) # 계산할 두 값 입력
arithmetics = Arithmetics() # 생성자 호출
print("뺼셈 : {}".format(arithmetics.minus(num_A,num_B))) # 원하는 기능 호출/뺄셈 결과값 호출
print("곱셈 : {}".format(arithmetics.multiply(num_A,num_B))) # 원하는 기능 호출/곱셈 결과값 호출
print("나눗셈 : {}".format(arithmetics.division(num_A,num_B))) # 원하는 기능 호출/나눗셈 결과값 호출