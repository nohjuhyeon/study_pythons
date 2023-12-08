#구구단 5단 단계별 표시(for문 사용)
def multiply(num_first,num_second):
    output = num_first * num_second
    pass
    return output

while True:
    try:
        num_input = input("단수:") #단수 입력
        num_first = int(num_input) #숫자로 변환
        if num_first == 30 or num_first == 35 or num_first == 20:
            for num_second in range(1,10):
                print("{} X {} = {}" .format(num_first,num_second,multiply(num_first,num_second)))
                pass
            pass
        else:
            print("20, 30, 35 외의 다른 숫자를 입력했습니다. 다시 입력해주세요.")
    except:
        if num_input == "q": #"q"일 경우 종료
            break
        else:
            print("20, 30, 35 외의 다른 문자를 입력했습니다. 다시 입력해주세요.")
            pass #"q"외의 다른 단어일 경우 계속 진행()

