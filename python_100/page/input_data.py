def input_data(int_or_string = "int"):
    if (int_or_string == "int"):
        return list(map(int, input().split(",")))
    else:
        return list(input().split(","))
    