
def isPrime(num):
    for i in range(2, int(num/2)):
        if (num % i == 0):
            return False
        return True

def main():
    while True:
        try:
            value = int(input())
        except:
            break

        number = value
        ranged = int((number ** (1/2))) + 1
        for i in range(2, ranged):
            count = 0
            if (number % i == 0):
                if (isPrime(i) == False):
                    continue
                else:
                    while(number % i == 0 or number == 0):
                        count += 1
                        number = number / i
            else:
                continue

            if (count == 1):
                print(i, end='')
            else:
                print(f"{i}^{count}",end='')

            if (number == 1):
                print()
                continue
            else:
                print(" * ", end='')
        
        if (number == value):
            print(number)
        elif (number > 1):
            print(int(number))
        
main()