def decimal(str):
    sum = 0
    for i in range(len(str)):
        sum += int(str[i]) * (2 ** i)
    return sum
    