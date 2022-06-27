#zerojudge : https://zerojudge.tw/ShowProblem?problemid=a410

def main():
    while True:
        try:
            a1, b1, c1, a2, b2, c2 = map(float, input().split())
        except:
            break

        delta = (a1 * b2 - a2 * b1)
        delta_x = (c1 * b2 - c2 * b1)
        delta_y = (a1 * c2 - a2 * c1)

        if (delta == 0):
            if (delta_x == 0 or delta_y == 0):
                print("Too many")
                continue
            else:
                print("No answer")
                continue
        else:
            x = round(delta_x / delta, 2)
            y = round(delta_y / delta, 2)
        print(f"x={'%.2f' % x}")
        print(f"y={'%.2f' % y}")

main()