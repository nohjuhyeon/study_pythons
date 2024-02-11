# function만 사용해 적 캐릭터 만들기 
# first 적 캐릭터
name = "first"  
hp1 = 120
damage1 = 0

def attack(health,damage):
    health = health - damage 
    return health

user1 = attack(hp1,damage1)
print(user1)
pass

# # function만 사용 시 제한 극복 -> class
# class Enemy:
#     def __init__(self, name, health):       #self.name = class의 name // name = 외부에서 들어온 name ///변수 앞에 self가 붙으면 class 내에서만 사용할 수 있는 변수로 만들 수 있음
#         self.name = name                    # 외부 변수 name 값이 class 내부 변수 self.name에 할당 
#         self.health = health
#         self.damage = 0 
#         pass

#     def function_name(self):
#         pass
#         return 0

#     def attack(self, damage):
#         self.health = self.health - damage
#         return self.health

# # first_enemy = Enemy()     # 자신의 자원(function과 variables) 확인 
# first_name = 'first'
# first_health = 150
# first_enemy = Enemy(first_name,first_health)     # 자신의 자원(function과 variables) 확인 
# Second_enemy = Enemy('Second',300)
# pass
# Enemy()