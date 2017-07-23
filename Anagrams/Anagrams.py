from math import factorial

def iter(moves, remchars, start):

    dup_count_fact = 1

    uniquechars = set(start)
    
    for i in uniquechars:
        if start.count(i) > 1:
            dup_count_fact *= factorial(start.count(i))

    return moves * factorial(remchars) / dup_count_fact

def listPosition(word):

    target = word + ""

    start = "".join(sorted(target))

    sum = 0

    for i in range(len(target) - 1):
        pos = start.find(target[i])
        start = start.replace(target[i], "", 1)
        sum += iter(pos, len(start), target[i:])

    sum += 1
    
    return sum

 
