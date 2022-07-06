class upper_case():
    def __init__(self):
        self.__string = ""
    def getString(self):
        self.__string = input()
        if (self.__string == ""):
            return 0
    def printString(self):
        print(self.__string.upper())


def main():
    string = upper_case()
    string.getString()
    string.printString()


main()