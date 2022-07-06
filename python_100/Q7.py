from page import input_data
def main():
    i, j = input_data.input_data()
    List_2D = [[x*y for x in range(j)] for y in range(i)]
    print(List_2D)

main()