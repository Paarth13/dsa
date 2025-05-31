def main():
    nums=[-1,0,1,2,-1,-4]
    nums.sort()
    lena=len(nums)
    ans=[]
    for i in range(lena-2):
        l,r=i+1,lena-1
        while l<r:
            val=nums[i]+nums[l]+nums[r]
            if val==0:
                ans.append([i,l,r])
            elif val>0:
                r-=1
            else:
                l+=1
        print("Out of Loop",i)
    return ans
if __name__=="__main__":
    print(main())
