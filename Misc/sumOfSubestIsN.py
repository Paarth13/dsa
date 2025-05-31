def ReturnPairIfExistsEqualSum(arr,sumVal):
    i,j=0,len(arr)-1
    while(i<j):
        if arr[i]+arr[j]>sumVal:
            j-=1
        elif arr[i]+arr[j]<sumVal:
            i+=1
        else:
            print (arr[i],arr[j])
            break
def main():
    sumVal=4
    arr=[1,1,3,4,5]
    ReturnPairIfExistsEqualSum(arr,sumVal)

if __name__ == "__main__":
    main()