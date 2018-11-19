# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

import sys

isInfix = True
infix, prefix = "", ""
for line in sys.stdin:
    if isInfix:
        infix = line.strip()
        isInfix = False
        continue
    else:
        prefix = line.strip()
        isInfix = True
