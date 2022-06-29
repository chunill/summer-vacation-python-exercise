# zerojudge: https://zerojudge.tw/ShowProblem?problemid=a005

def main():
    while True:
        sequence = []
        try:
            num = int(input())
            for i in range(num):
                sequence.append(list(map(int, input().split())))
        except:
            break

        for i in range(num):
            if (sequence[i][1] - sequence[i][0] == 0):
                ratio = 0
            else:
                ratio = (sequence[i][2] - sequence[i][1]) / (sequence[i][1] - sequence[i][0])

            for j in sequence[i]:
                print(j, end=' ')
            print(int(sequence[i][3] + ((sequence[i][3] - sequence[i][2]) * ratio)))

main()