def main():
    num = int(input())
    sum = 0
    for i in range(4):
        digit = 0
        for j in range(3 - i, -1, -1):
            digit += 9 * (10 ** j)
        sum += digit
            
    print(sum)

main()