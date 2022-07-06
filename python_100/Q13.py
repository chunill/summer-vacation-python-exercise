from curses.ascii import isalpha, isdigit


def main():
    string = input()
    alpha = 0
    num = 0
    for i in range(len(string)):
        if isalpha(string[i]) :
            alpha += 1
        elif isdigit(string[i]):
            num += 1
    print("LETTERS", alpha)
    print("DIGITS", num)


main()