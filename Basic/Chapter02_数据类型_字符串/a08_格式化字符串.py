#!/usr/bin/python3
# -*- coding=utf-8 -*-


# info_tuple = ("小明", 19, 1.75)
# str = "{}.{} and {}".format(*info_tuple)

str1 = "1"
str2 = 12.3456
str3 = "hello"

# str = "%s and %.05f and %s" %(str1, str2, str3)
# str = "{} and {:.05f} and {}".format(str1, str2, str3)
str = f"{str1} and {str2:.05f} and {str3}"

print(str)

print("=" * 30)