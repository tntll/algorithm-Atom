def conflict(state, pos):
    nextY = len(state)
    if pos in state:
        return True
    for i in range(nextY):
        if nextY - pos == i - state[i]:
            return True
        if nextY + pos == i + state[i]:
            return True
    return False


def queens(num, state=()):
    if num-1 == len(state):
        for i in range(num):
            if not conflict(state, i):
                yield (i,)
    else:
        for pos in range(num):
            if not conflict(state, pos):
                for result in queens(num, state+(pos,)):
                    yield (pos,) + result


for i in list(queens(8)):
    print(i)
