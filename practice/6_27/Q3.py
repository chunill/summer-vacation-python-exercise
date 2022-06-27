def main():
    while True:
        try:
            value = int(input())
        except:
            break

        number = value
        ranged = int((number ** (1/2))) + 1
        for i in range(2, ranged):
            power = 0
            while(number % i == 0):
                power += 1
                number = number / i

            if (power == 0):
                continue
            if (power == 1):
                print(i, end='')
            else:
                print(f"{i}^{power}",end='')

            if (number == 1):
                print()
                break
            else:
                print(" * ", end='')
        
        if (number == value):
            print(number)
        elif (number > 1):
            print(int(number))
        
main()