from Q1 import random_number_list as rnl
import time
def find_min(index, List):
    min_index = index
    for i in range(index, len(List)):
        if List[i] < List[min_index]:
            min_index = i
    return min_index

def selection_sort():
    while True:
        try:
            List_len = int(input("Enter the list length >> "))
            sort_time = int(input("Enter the sort time >> "))
            test_time = int(input("Enter the test time >> "))
        except:
            break
        
        print()
        for _ in range(test_time):
            time_start = time.time()
            for _ in range(sort_time):
                List = rnl(1,100,List_len)
                for i in range(List_len - 1):
                    min_index = find_min(i, List)
                    List[i], List[min_index] = List[min_index], List[i]
                    
            time_end = time.time()
            print("total run time:", '%.2f' % (time_end - time_start), "s")
            print("average run time:", '%.2f' % ((time_end - time_start) * 1000 / sort_time), "ms")
            print("")


selection_sort()