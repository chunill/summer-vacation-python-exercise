from page import number_operate as no

def main():
    print("divisible by 7 but are not a multiple of 5, between 2000 and 3200:")
    List = no.between(2000, 3200, 7, 5)
    print(*List, sep=",")
            

main()