

def between(start, end, number = 1, other = 1):
    if other == 1:
        return [x for x in range(start, end)]
    else :
        return [x for x in range(start, end, number) if x % other == 0]

def factorial(N):
    sum = 1
    for i in range(2, N+1):
        sum *= i
    return sum