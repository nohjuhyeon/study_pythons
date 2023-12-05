# quests 
# BMI = 몸무게(kg) / 키(m^2)
# BMI 분류
# 18 미만: 저체중
# 18 - 22: 정상
# 23 - 24 : 과체중
# 25 이상 : 비만

str_weight  = "몸무게: "
str_height = "키 :"
weight = int(input("{}" .format(str_weight)))
height = int(input("{}" .format(str_height)))

bmi = int(weight / ((height/100)**2))
if bmi < 18:
    print("{}은 18 미만으로 저체중입니다.".format(bmi))
elif bmi <23:
    print("{}은 23 미만으로 정상입니다.".format(bmi))
elif bmi < 25:
    print("{}은 25 미만으로 과체중입니다.".format(bmi))
else :
    print("{}은 25 이상으로 비만입니다.".format(bmi))


