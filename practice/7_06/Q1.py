import random
def random_number_list(start, end, length):
    List = [x for x in range(start,end + 1)]
    List = random.sample(List, length)
    return List

