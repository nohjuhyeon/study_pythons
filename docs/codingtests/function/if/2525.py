# https://www.acmicpc.net/problem/2525
# 문제
## KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다. 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산한다.
## 또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다.
## 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.
# 출력
## 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)

class Question:
    def __init__(self):
        list_input = list(map(int, input().split()))                            # list_input = 현재 시각을 시와 분으로 입력 받아 리스트로 지정
        self.input_hour = list_input[0]                                         # input_hour = 입력한 시각의 시
        self.input_minute = list_input[1]                                       # input_minute = 입력한 시간의 분
        self.time_input =int(input())                                           # time_input = 요리하는 데 필요한 시간
        self.time_hour = int(self.time_input/60)                                # time_hour, time_minute = time_input을 시와 분으로 나눠서 변수 지정
        self.time_minute = (self.time_input%60)
        pass

    def time(self):
        if self.input_minute + self.time_minute < 60:                           # 현재 시각의 분과 필요한 시간의 분의 합이 60이 안 될 경우
            output_hour = self.input_hour + self.time_hour                      # 종료되는 시각의 시 = 현재 시각의 시 + 요리하는 데 필요한 시간의 시
            output_minute = self.input_minute + self.time_minute                # 종료되는 시각의 분 = 현재 시각의 분 + 요리하는데 필요한 시간의 분
        elif self.input_minute + self.time_minute == 60:                        # 현재 시각의 분과 필요한 시간의 분의 합이 60일 경우
            output_hour = self.input_hour + self.time_hour + 1                  # 종료되는 시각의 시 = 현재 시각의 시 + 요리하는 데 필요한 시간의 시 + 1
            output_minute = 0                                                   # 종료되는 시각의 분 = 0
        else:                                                                   # 현재 시각의 분과 필요한 시간의 분의 합이 60이 넘을 경우
            output_hour = self.input_hour + self.time_hour + 1                  # 종료되는 시각의 시 = 현재 시각의 시 + 요리하는 데 필요한 시간의 시 + 1
            output_minute = self.input_minute + self.time_minute - 60           # 종료되는 시각의 분 = 현재 시각의 분 + 요리하는데 필요한 시간의 분 - 60
        pass
        if output_hour >= 24:                                                   # 종료되는 시각의 시가 24가 넘을 경우
            output_hour = output_hour - 24                                      # 종료되는 시각의 시 - 24
        print("{} {}".format(output_hour, output_minute))                       # 종료되는 시각 출력

quest = Question()

quest.time()