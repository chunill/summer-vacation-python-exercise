from page import binary, input_data
def main():
    List = input_data.input_data("str")

    for i in List:
        if binary.decimal(i) % 5 == 0:
            print(i)
            


main()