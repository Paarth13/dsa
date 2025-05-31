"""This can be generic solution to find a unique element when the other elements are repeated N times """ 

def FindTheUniqueElement(arr,elementsRepeated):
    ans=0
    for i in range(0,4):
        count=0
        for j in range(0,len(arr)):
            if arr[j]&(1<<i):
                count+=1
        if count%elementsRepeated!=0:
            ans=ans|(1<<i)
    print(ans)


def main():
    arr=[1,1,1,2,2,2,3,4,4,4]
    elementsRepeated=3
    FindTheUniqueElement(arr,elementsRepeated)
if __name__ == "__main__":
    main()