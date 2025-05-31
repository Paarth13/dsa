def BS(A,start,end,val):
    ans=0
    while start<=end:
        m=(start+end)//2
        if A[m]==val:
            return m
        elif A[m]>val:
            end=m-1
        else:
            ans=start
            start =m+1
    return ans

def find_ans(A,start,end):
    lena=len(A)-1
    # print
    ind1,ind2=BS(A,0,lena,end),BS(A,0,lena,start)
    if ind1==ind2 and ind1==0:
        print (0)
        return 
    print (ind1-ind2+1,ind1,ind2)

def main():
    listOfNums=[6,5,7,8,100]
    find_ans(listOfNums,2,400)
if __name__=="__main__":
    main()