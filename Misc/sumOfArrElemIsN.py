# Given an array of +ve integers and a +ve integer nprint all the pairs who's sum is n  
# test cases [1,9,10,12] ,10 output=[1,9]
# test cases [1,9,1,9] ,10 output=[1,9],[1,9]
def sumPairEqualToN(ar,n):
    # ar=ar.sort()
    f=0
    i=0
    while i<len(ar):
        j=i+1
        while j<len(ar):
            if ar[i]+ar[j]==n:
                print(ar[i]," ",ar[j])
                ar.remove(ar[i])
                ar.remove(ar[j-1])
                f=1
                print (ar)
                break
            j+=1 
        if f==1:
            i=0
            f=0
        else:
            i+=1
def main():
    ar=[1,9,1]
    n=10
    sumPairEqualToN(ar,n)
if __name__ == "__main__":
    main()