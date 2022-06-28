# zerojudge: https://zerojudge.tw/ShowProblem?problemid=b266

def rotate(R, C, list_2D: list):
    new_list = []
    for i in range(C-1, -1, -1):
        add_list = []
        for j in range(R):
            add_list.append(list_2D[j][i])
        new_list.append(add_list)
    Z = R
    R = C
    C = Z
    return R, C, new_list

def flip(R, list_2D: list):
    new_list = []
    for i in range(R-1, -1, -1):
        new_list.append(list_2D[i])
    return new_list

def main():
    while True:
        array = []
        try:
            R, C, M = map(int, input().split())
            for i in range(R):
                array.append(list(map(int, input().split())))
            way = list(map(int, input().split()))
        except:
            break
        for i in range(len(way)-1, -1, -1):
            if (way[i] == 0):
                R, C, array = rotate(R, C, array)
            elif (way[i] == 1):
                array = flip(R, array)
        print(R, C)
        for i in range(R):
            for j in range(C):
                print(array[i][j], end=' ')
            print()
    
main()