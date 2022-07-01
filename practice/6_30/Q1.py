def is_palin(List: list):
    set_list = list(set(List))
    odd = 0
    for i in range(len(set_list)):
        if (List.count(set_list[i]) % 2 == 0):
            pass
        elif (odd == 0):
            odd = 1
        else:
            return False
    return True

def main():
    while True:
        try:
            List = input()
        except:
            break
        alpha_list = [k.lower() for k in List if k.isalpha()]
        
        if (is_palin(alpha_list)):
            print("yes !")
        else:
            print("no...")
        
main()