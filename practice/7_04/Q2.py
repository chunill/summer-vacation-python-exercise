def main():
    while True:
        try:
            N = int(input())
        except:
            break
        for non in range(N):
            X, a, b = map(int, input().split())
            check = False
            start = X % a
            end = X + 1
            for i in range(start, end, a):
                if (i % b == 0):
                    print(int((X - i) / a + (i / b)))
                    check = True
                    break
            if (check == False):
                print(-1)

main()