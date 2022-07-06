def main():
    sum = 0
    while True:
        try:
            C, num = input().split()
        except:
            break
        num = int(num)
        if C == "D":
            sum += num 
        elif C == "W":
            sum -= num
    print(sum)
        

main()