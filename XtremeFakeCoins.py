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

def pairs(source):
    result = []
    for p1 in range(len(source)):
        for p2 in range(p1+1,len(source)):
            result.append([source[p1],source[p2]])
    return result

class Weighting:
    def __init__(self, left, right):
        self.left = left
        self.right = right

N, M = get_word().split(',')
N, M = int(N), int(M)

w = []
for m in range(M):
    left, right = get_word().split('-')
    w.append(Weighting(left, right))

dictionary = {}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = letters[:N]

for n in range(N):
    dictionary[letters[n]] = 1

pairs = pairs(letters)

p = []
for i in range(len(pairs)):
    p.append(str(pairs[i][0]) + str(pairs[i][1]))
    # print(p[i])

# source = pairs(p)

result = []
for p1 in range(len(p)):
    for p2 in range(p1+1,len(p)):
        result.append([p[p1],p[p2]])

for i in range(len(result)):
    curr1, curr2 = result[i][0], result[i][1]
    # print(curr1, curr2)
    if (curr1[0] == curr2[0]):
        dictionary[curr1[0]] = 0
        dictionary[curr2[0]] = 0
    elif (curr1[1] == curr2[1]):
        dictionary[curr1[1]] = 0
        dictionary[curr2[1]] = 0
    else:
        dictionary[curr1[0]] = 0
        dictionary[curr1[1]] = -1
        dictionary[curr2[0]] = -1
        dictionary[curr2[1]] = 0
    # print (curr1, curr2)
    for m in range(M):
        sum1, sum2 = 0, 0
        for j in range(len(w[m].left)):
            sum1 = sum1 + dictionary[w[m].left[j]]
            sum2 = sum2 + dictionary[w[m].right[j]]
        # print(sum1, sum2)
        # print(sum1, sum2)
        if (sum1 == sum2):
            if (curr1[0] == curr2[0]):
                dictionary[curr1[0]] = 0
                dictionary[curr2[0]] = 0
            elif (curr1[1] == curr2[1]):
                dictionary[curr1[1]] = 0
                dictionary[curr2[1]] = 0
            else:
                dictionary[curr1[0]] = 0
                dictionary[curr1[1]] = -1
                dictionary[curr2[0]] = -1
                dictionary[curr2[1]] = 0
            print(curr1 + '=' + curr2)
            break
        if (m == M-1):
            if (curr1[0] == curr2[0]):
                dictionary[curr1[0]] = 0
                dictionary[curr2[0]] = 0
            elif (curr1[1] == curr2[1]):
                dictionary[curr1[1]] = 0
                dictionary[curr2[1]] = 0
            else:
                dictionary[curr1[0]] = 0
                dictionary[curr1[1]] = -1
                dictionary[curr2[0]] = -1
                dictionary[curr2[1]] = 0
