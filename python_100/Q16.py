def main():
    List = list(map(int, input().split(",")))
    final_List = []
    for i in List:
        if i % 2 != 0:
            final_List.append(i * i)
    print(*final_List, sep=",")


main()