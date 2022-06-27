# zerojudge : http://zerojudge.tw/ShowProblem?problemid=a004

def main():
    while True:
        try:
            year = int(input())
        except:
            break
        if (year % 100 == 0 and year % 400 != 0):
            print("平年")
            continue
        elif (year % 4 == 0):
            print("閏年")
            continue
        print("平年")

main()