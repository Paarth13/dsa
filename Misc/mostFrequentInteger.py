def freqNum(arr):
    dictNum={}
    maxVa=[-999999,-999999]
    for i in range(0,len(arr)):
        if dictNum.get(arr[i]):
            dictNum[arr[i]]+=1
        else:
            dictNum[arr[i]]=1
        if dictNum[arr[i]]>maxVa[1]:
            maxVa=[arr[i],dictNum[arr[i]]]
    return maxVa
def main():
    ar=[1,1,34,5,5,5,7,2,1,5,5,6,2,1,1]
    print(freqNum(ar))
if __name__ == "__main__":
    main()