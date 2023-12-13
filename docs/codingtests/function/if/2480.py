# https://www.acmicpc.net/problem/2480
# 문제
## 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
## 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
## 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
## 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
## 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
## 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
# 입력
## 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
# 출력
## 첫째 줄에 게임의 상금을 출력 한다.

class Quest:
    def __init__(self):
        self.input_dice = list(map(int,input().split()))                        # 입력한  주사위 세 개를 리스트에 넣기
        self.dice_first = self.input_dice[0]                                    # 첫번째 주사위 변수 지정
        self.dice_second = self.input_dice[1]                                   # 두번째 주사위 변수 지정
        self.dice_third = self.input_dice[2]                                    # 세번째 주사위 변수 지정

    def check(self):
        if self.dice_first == self.dice_second == self.dice_third:              # 주사위 세 개 값이 다 같을 경우
            check = 3                                                           # 비교 결과를 3으로 지정
            list_check = self.dice_first                                        # 주사위 세 개 중 하나가 대표값
        elif self.dice_first == self.dice_second:                               # 주사위 세 개 중 두 개가 같을 경우
            check = 2                                                           # 비교 결과를 2로 지정
            list_check =self.dice_first                                         # 같은 값 중 하나가 대표값
        elif self.dice_first == self.dice_third:                                # 주사위 세 개 중 두 개가 같은 경우
            check = 2                                                           # 비교 결과를 2로 지정
            list_check = self.dice_first                                        # 같은 값 중 하나가 대표값
        elif self.dice_second == self.dice_third:                               # 주사위 세 개중 두 개가 같은 경우
            check = 2                                                           # 비교 결과를 2로 지정
            list_check = self.dice_second                                       # 같은 값 중 하나가 대표값 
        else:                                                                   # 주사위 세 개 값이 다 다들 경우
            check = 1                                                           # 비교 결과를 1로 지정
            list_check = max(self.dice_first,self.dice_second,self.dice_third)  # 주사위 세 개 중 가장 큰 값이 대표값
        return check,list_check                                                 # 비교 결과와 대표값 리턴
    
    def price(self,check,list_check):
        if check == 1:                                                          # 비교 결과가 1일 경우
            print(list_check * 100)                                             # 대표값 * 100
        elif check == 2:                                                        # 비교 결과가 2일 경우
            print(list_check * 100 + 1000)                                      # 대표값 * 100 + 1000
        elif check == 3:
            print(list_check * 1000 + 10000)                                    # 대표값 * 1000 + 10000

quest = Quest()
check,list_check = quest.check()
pass
quest.price(check,list_check)
pass

