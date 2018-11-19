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

n = get_number()
arr = []
guess = bin((1<<n)-1)
print('Q '+' '.join(guess[2:]))

interaction = get_number()
ones = interaction

# interaction = 1
arr.append(interaction)
AnswerFound = False

if (interaction == n):
    print('A '+' '.join(guess[2:]))
else:
    for i in range(n-1):
        guess = bin((1<<n)-(1<<(i+1)))
        print('Q '+' '.join(guess[2:]))
        interaction = get_number()
        if (interaction == n):
            print('A '+' '.join(guess[2:]))
            AnswerFound = True
            break
        arr.append(interaction)

if not AnswerFound :
    cnt = 0
    final_guess = []
    # final_guess.append(0)
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            final_guess.append(str(0))
        else:
            final_guess.append(str(1))
            cnt += 1
    final_guess.reverse()
    extra = []
    if (ones != cnt):
        extra.append(str(1))
    else:
        extra.append(str(0))
    answer = extra + final_guess

    print('A '+' '.join(answer))
