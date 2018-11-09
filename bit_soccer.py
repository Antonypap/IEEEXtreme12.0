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

def totalSum(a, t):
    sum = []
    for i in range(len(a)):
        sum1 = 0
        for j in range(i, len(a)):
            sum1 = (sum1 | a[j]);
            if(sum1 == t):
                return "YES"
    return "NO";

N = get_number()

P = []
for i in range(N):
    P.append(get_number())

P.sort()

q = get_number()

for query in range(q):
    G = get_number()


# Driver code
    print(totalSum(P, G))
