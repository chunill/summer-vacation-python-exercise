"""
Q3:
讀取json檔案，並且輸出default中的每個key供使用者選擇
並提示使用者輸入欲查詢的key，輸出該key下的text、placeholder、hint_text的值
"""
import json


def main():
    with open("practice/6_29/Q3.json", "r", encoding = "utf-8") as file:
        data = json.load(file)

    ATK = data["default"]
    list_key = list(ATK.keys())
    print("key list >> ")
    print()
    for i in range(len(list_key)):
        print(i, ":", list_key[i])
    print()
    query_key = list_key[int(input("Enter the key to query num>> "))]
    print()
    ATK = ATK[query_key]
    list_key = list(ATK.keys())

    print("key :", query_key)
    for i in list_key:
        print(i, ":", ATK[i])
    print()

    
main()