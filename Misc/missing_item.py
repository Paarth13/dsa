def miss_item(fullList,HalfList):
    missing_value=0
    for num in fullList:
        missing_value^=num
    for num in HalfList:
        missing_value^=num
    return missing_value
def main():
    print (miss_item([1,2,4,56,7],[1,2,4,7]))
if __name__ == "__main__":
    main()