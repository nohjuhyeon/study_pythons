#구구단 5단 단계별 표시(for문 사용)
def multiply(num_first,num_second):
    output = num_first * num_second
    pass
    return output

while True:
    try:
        num_input = input("단수:") #단수 입력
        num_first = int(num_input) #숫자로 변환
        for num_second in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("{} X {} = {}" .format(num_first,num_second,multiply(num_first,num_second)))
            pass
        pass
    except:
        if num_input == "q": #"q"일 경우 종료
            break
        else:
            pass #"q"외의 다른 단어일 경우 계속 진행

