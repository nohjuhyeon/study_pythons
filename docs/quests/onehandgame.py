str_first = "1"
str_second = ""
str_third = "2"
str_fourth =""
str_fifth = "3"
print(" {}, {}, {}, {}, {}" .format(str_first, str_second, str_third, str_fourth, str_fifth))
str_first, str_second = str_second, str_first
print(" {}, {}, {}, {}, {}" .format(str_first, str_second, str_third, str_fourth, str_fifth))
str_third, str_fourth = str_fourth, str_third
print(" {}, {}, {}, {}, {}" .format(str_first, str_second, str_third, str_fourth, str_fifth))
str_third, str_fifth = str_fifth, str_third
print(" {}, {}, {}, {}, {}" .format(str_first, str_second, str_third, str_fourth, str_fifth))
str_first, str_third = str_third, str_first
print(" {}, {}, {}, {}, {}" .format(str_first, str_second, str_third, str_fourth, str_fifth))
str_second, str_third  = str_third, str_second
print(" {}, {}, {}, {}, {}" .format(str_first, str_second, str_third, str_fourth, str_fifth))
str_third, str_fifth = str_fifth, str_third
print(" {}, {}, {}, {}, {}" .format(str_first, str_second, str_third, str_fourth, str_fifth))
str_fourth, str_third = str_third, str_fourth
print(" {}, {}, {}, {}, {}" .format(str_first, str_second, str_third, str_fourth, str_fifth))