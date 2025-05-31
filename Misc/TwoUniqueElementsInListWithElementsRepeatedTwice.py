"""
To keep in mind:
1. When we xor all the values we get a solution with X^Y.
2. Answer to X^Y will have a set value in its bit form where there is a diff in bit values of X and Y.
3. Picking that bit position we segregate the original list into two lists with that same bit as set.
4. Now it becomes a simple solution of same elements occuring twice and find unique one.
 For deeper understanding make table of list in bits and segregate the two lists.  
"""
def FindTheUniqueElement(arr):
    xorSol=0
    setBitPos=0
    for i  in range(0,len(arr)):
        xorSol^=arr[i]
    i=0
    print (xorSol)
    while(1):
        if xorSol&(1<<i)!=0:
            break
        i+=1
        setBitPos+=1
    elementOne,elementTwo=0,0
    # lisWithSetBit,lisWithUnsetBit=[],[]
    for i  in range(0,len(arr)):
        if arr[i] & (1<<setBitPos):
            elementOne^=arr[i]
        else:
            elementTwo^=arr[i]
    print (elementTwo,elementOne)
def main():
    arr=[1,1,2,2,3,5,4,4]
    FindTheUniqueElement(arr)
if __name__ == "__main__":
    main()