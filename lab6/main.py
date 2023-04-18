#!/usr/bin/env python3

import sys
import re
def replace_digits(number):
    retNumber = 0
    position = 1
    while number > 0:
        digit = number % 10
        new_digit = (digit * 9 + 1) % 10
        retNumber += new_digit * position
        position *= 10
        number //= 10
    return retNumber

def my_printf(format_string,param):
    REGEX = r'#(\d+)?g'
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#':
                result = re.search(REGEX, format_string[idx:])
                first = result.group(1)
                if first and param.isnumeric():
                    firstInt = int(first)
                    nowa_liczba = ""
                    for cyfra in param:
                        if cyfra == "0":
                            nowa_liczba += "9"
                        else:
                            nowa_liczba += str(int(cyfra)-1)
                    print(f'{nowa_liczba:>{firstInt}}',end="")
                elif first and not param.isnumeric():
                    firstInt = int(first)
                    print(f'{param:>{firstInt}}',end="")
                elif first and format_string[idx+1]  == 'g':
                    nowa_liczba = ""
                    for cyfra in param:
                        if cyfra == "0":
                            nowa_liczba += "9"
                        else:
                            nowa_liczba += str(int(cyfra)-1)
                    print(f'{nowa_liczba:>{firstInt}}',end="")
                else:
                    break
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            if format_string[idx] == 'g':
                shouldDo=True
    print("")


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
