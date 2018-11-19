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


def totalSum(a, t):
    for i in range(len(a)):
        sum1 = 0
        for j in range(i, len(a)):
            sum1 = (sum1 | a[j])
            if(sum1 == t):
                return "YES"
    return "NO"

N = get_number()
P = []
for i in range(N):
    a = get_number()
    P.append(a)

q = get_number()
sorted(P)
for pp in range(q):
    G = get_number()
    print(totalSum(P, G))
