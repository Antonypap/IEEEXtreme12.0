import sys

class Player:

    def __init__(self, id):
        self.id = id
        self.pos = 0

class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self,data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0,data)
          return True
      return False

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)

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

def index(p, size):
    i, j = p
    if (j % 2 != 0):
        return (i+(j-1)*size)
    else:
        return (5-i+(j-1)*size)

def inv(index, size):
    if (((index - 1)// size) % 2 == 0):
        j = ((index-1) // size) + 1
        i = index % size
    else:
        j = ((index-1) // size) + 1
        i = (size -(index % size) + 1) % size
    return (i,j)

B = get_number()

P = get_number()
players = []
q = Queue()
for player in range(P):
    p = Player(player)
    players.append(p)
    q.enqueue(p)

S = get_number()
shead = []
stail = []
for snake in range(S):
    h1 = get_number()
    h2 = get_number()
    shead.append(index((h1, h2), B))
    t1 = get_number()
    t2 = get_number()
    stail.append(index((t1, t2), B))

L = get_number()
lstart = []
lend = []
for ladder in range(L):
    s1 = get_number()
    s2 = get_number()
    lstart.append(index((s1, s2), B))
    e1 = get_number()
    e2 = get_number()
    lend.append(index((e1, e2), B))

# for l in range(L):
#     for s in range(S):
#         if (lend[l] == shead[s]):
#             lend[l] = stail[s]
#         if (stail[s] == lstart[l]):
#             stail[s] = lend[l]
#
start = lstart + shead
end = lend + stail
print(start)
print(end)

K = get_number()
for i in range(K):
    if (q.size() == 0):
        break
    d1, d2 = get_number(), get_number()
    dice = d1 + d2

    p = q.dequeue()

    p.pos += dice

    if (p.pos >= B*B + 1):
        p.pos = -1
        players[p.id] = p
        continue

    for j in range(len(start)):
        if (p.pos == start[j]):
            p.pos = end[j]
            # break

    players[p.id] = p
    q.enqueue(p)

for p in players:
    sys.stdout.write(str(p.id+1))
    sys.stdout.write(' ')
    if (p.pos == -1):
        sys.stdout.write('winner')
    else:
        i, j = inv(p.pos, B)
        sys.stdout.write(str(i))
        sys.stdout.write(' ')
        sys.stdout.write(str(j))
    print()

# print(index((1,2), 4))
# print(inv(1, 4))
