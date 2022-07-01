import random

class BoxOfProduce:
    def __init__(self):
        self.__produce = ["Broccoli", "Tomato", "Kiwi", "Kale", "Tomatillo"]
        self.__box = [self.__produce[random.randint(0,4)] for i in range(3)]
    def getBox(self):
        return self.__box
    def setBox(self, box_old_index, produce_new_index):
        self.__box[box_old_index] = self.__produce[produce_new_index]
    def getProduce(self):
        return self.__produce
    def outputBox(self):
        [print(i, self.__box[i]) for i in range(3)]
    
def main():
    box = BoxOfProduce()
    old_index = 0
    new_index = 0
    
    while(True):
        print("Your box:")
        box.outputBox()
        print()
        yn = input("Do you replace item? (y/n) >> ")
        if (yn == "y"):
            old_index = int(input("Enter the index to item of box >> "))
            print()
            print("The produce list: ")
            for i in range(5):
                print(i,":", box.getProduce()[i])
            print()
            new_index = int(input("Enter the index to item of produce list >> "))
            box.setBox(old_index, new_index)
        elif (yn == "n"):
            break
        else:
            print("Enter try again!")
    print()
    print("Your box:")
    box.outputBox()

main()