def main():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
        except:
            break
        print(*[n for n in range(n) if n % 7 != 0])

main()