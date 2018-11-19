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

def printPairs(arr, arr_size, sum):

    # Create an empty hash set
    s = set()
    ok = False
    for i in range(0,arr_size):
        temp = sum-arr[i]
        if (temp in s):
            x, y  = arr[i], temp
            ok = True
            if (x > y):
                x, y = y, x
            print(x, y)
            break
        s.add(arr[i])
    if (not ok):
        print("!OK")

T = get_number()

for _ in range(T):
    SUM = get_number()
    E = get_number()
    array = []
    for e in range(E):
        array.append(get_number())

    printPairs(array, E, SUM)
