#!/usr/bin/env python3

import sys
import re


def my_printf(format_string,param):
    x = re.search("#\.\d+g", format_string)
    param = str(replace(int(param)))
    if x:
        format = x.group()
       	num = format[2:-1]
        if num.isnumeric():
            s = param.rjust(int(num), '0')
            x = re.sub("#\.\d+g", s, format_string)
            print(x)
            return
    print(format_string)
    
def replace(number):
    position = 1
    retNumber = 0
    while number > 0:
        digit = number % 10
        new_digit = (digit * 9 + 1) % 10
        retNumber += new_digit * position
        position *= 10
        number //= 10
    return retNumber


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
