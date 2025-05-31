def palinCount(stringCount):
    if stringCount==stringCount[::-1]:
        return 0
    # countOfDelFromFront=0
    lengthOfString=len(stringCount)
    # countOfDelFromBack=0
    countValue=0
    newStringForPalin=stringCount
    while (1):
        countValue+=1
        stringForFront=stringCount[countValue:]
        if len(stringForFront)==1:
            break
        stringFromBack=stringCount[:lengthOfString-countValue]
        print ("String from Front",stringForFront)
        if stringForFront==stringForFront[::-1] and len(stringForFront)!=1 :
            break
        print ("String from Back",stringFromBack)
        if stringFromBack==stringFromBack[::-1] and len(stringFromBack)!=1:
            break
        # newStringForPalin=newStringForPalin+stringCount[lengthOfString-countValue-1]
        # print ("New String",newStringForPalin)
        # if newStringForPalin==newStringForPalin[::-1]:
        #     break
    return countValue
def main():
    print (palinCount("abcd"))

if __name__ == "__main__":
    main()