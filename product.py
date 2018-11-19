import numpy as np

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

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

N = get_number()
M = get_number()

A = []
B = []

for i in range(N):
    A.append(get_number())

for i in range(M):
    B.append([get_number()])

print(A)
print(B)

C = []

C = np.dot(A,B)

print(C)

# print(max_subarray(C))
