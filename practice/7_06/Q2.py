from Q1 import random_number_list as rnl
import time

def insertion_sort():
    while True:
        try:
            List_len = int(input("Enter the list length >> "))
            sort_time = int(input("Enter the sort time >> "))
            test_time = int(input("Enter the test time >> "))
        except:
            break
        
        for k in range(test_time):
            time_start = time.time()
            for _ in range(sort_time):
                List = rnl(1,100,List_len)
                for i in range(1, List_len):
                    insert = List[i]
                    j = i - 1
                    while (j >= 0 and insert < List(j)):
                        List[j+1] = List[j]
                        j -= 1
                    List[j+1] = insert
            time_end = time.time()
            print("total run time:", '%.2f' % (time_end - time_start), "s")
            print("average run time:", '%.2f' % ((time_end - time_start) * 1000 / sort_time), "ms")
            print("")

insertion_sort()


