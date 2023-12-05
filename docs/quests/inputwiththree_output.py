#quest
#가로  * 세로 * 높이 = 직육면체
#input: 가로 세로 높이
#output: 가로(4)m * 세로(1)m * 높이(1)m = 직육면체(4)m^3

num_first,num_second,num_third = input().split()
first = int(num_first)
second = int(num_second)
third = int(num_third)
cuboid = first * second * third
print("가로({})m * 세로({})m * 높이({})m = 직육면체({})m^3" .format(first, second, third, cuboid))