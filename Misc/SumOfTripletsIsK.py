def find_triplets(arr,val,lena):
    count=0
    for i in range(lena):
        temp_val=val-arr[i]
        start,end=i+1,lena-1
        while start<end:
            sum_val=arr[start]+arr[end]
            if sum_val<=temp_val:
                count+=end-start
                start+=1
            else:
                end-=1
    print(count)
def main():
    arr=[1,2,3,4,6]
    val=8
    lena=len(arr)
    find_triplets(arr,val,lena)
if __name__=="__main__":
    main()