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

class StarInfo:
    def __init__(self, S, F, D):
        self.S = S
        self.F = F
        self.D = D

    def __str__(self):
        return str(self.S) + ' ' + str(self.F) + ' ' + str(self.D)

Stars = []
N = get_number()
for n in range(N):
    s = get_number()
    f = get_number()
    d = get_number()
    star = StarInfo(s,f,d)
    Stars.append(star)
