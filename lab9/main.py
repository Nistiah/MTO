
import sys
import re

def my_printf(format_string,param):
    param = str(hex(int(param)))[2:]
    param = param.replace("a","g")
    param = param.replace("b","h")
    param = param.replace("c","i")
    param = param.replace("d","j")
    param = param.replace("e","k")
    param = param.replace("f","l")
    param = param.replace("0","o")
    
    x = re.search("#\.\d+j", format_string)
    
    if x:
        formatt = x.group()
       	num = formatt[2:-1]
       	param = param.rjust(int(num), 'o')
        x = re.sub("#\.\d+j",param, format_string)
        print(x)
        return
            
    print(format_string)

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
