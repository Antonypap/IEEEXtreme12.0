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

N = get_number()
M = get_number()
S = get_number()

now = 1
found = False
dp = []
dp.append(0)
dp.append(0)
dp.append(0)
dp.append(2*M+S)
# dp[0] = 0
# dp[1] = 0
# dp[2] = 0
# dp[3] = 2*M + S

for i in range(4,N):
    dp.append(dp[i-1] + (i//2)*M + S)
print(dp[N-1])
