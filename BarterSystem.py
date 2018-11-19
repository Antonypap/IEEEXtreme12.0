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

class GivenExch:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def __str__(self):
        return self.a + ' ' + self.b + ' ' + str(self.r)

class Queries:

    def __init__(self, k, l):
        self.k = k
        self.l = l

    def __str__(self):
        return self.k + ' ' + self.l

R = 998244353

N = get_number()
exchange = []
hash = {}
for n in range(N):
    a, b, r = get_word(), get_word(), get_number()
    hash[a] = r
    exchange.append(GivenExch(a, b, r))
    print(exchange[n])

Q = get_number()
queries = []
for q in range(Q):
    k, l = get_word(), get_word()
    queries.append(Queries(k, l))
    print(queries[q])
