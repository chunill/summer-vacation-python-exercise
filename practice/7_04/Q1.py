H = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
E = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]

def main():
    global H,E
    while True:
        try:
            year = int(input())
        except:
            break
        print(H[((year - 3) % 10) - 1] + E[((year - 3) % 12) - 1])

main()