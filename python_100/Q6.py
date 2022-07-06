from page import input_data
def main():
    for i in input_data.input_data():
        print(int((i * 10 / 3) ** (1 / 2)))
    

main()