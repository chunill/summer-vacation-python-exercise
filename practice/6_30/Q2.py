def main():
    while True:
        try:
            num = int(input())
            numList = list(map(int, input().split()))
        except:
            break
        list_2D = [[] for i in range(10)]
        for i in range(num):
            strA = numList[i]
            list_2D[strA % 10].append(strA)
        for i in list_2D:
            if i == []:
                continue
            print(*sorted(i, reverse=True), end=' ')
        print()
main()
