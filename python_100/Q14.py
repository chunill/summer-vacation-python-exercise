def main():
    string = input()
    upp = 0
    low = 0
    for i in string:
        if not i.isalpha():
            continue
        if i.isupper():
            upp += 1
        else:
            low += 1

    print("UPPER", upp)
    print("LOWER", low)

main()