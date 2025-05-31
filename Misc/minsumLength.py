class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        i,j=0,0
        lena=len(arr)
        curr_val=0
        ans=[]
        while i<lena and j<lena:
                # if arr[i]==target:
                #     ans.append(1)
                #     i+=1
         
                if curr_val==target:
                    ans.append(j-i) if j!=i else ans.append(1)
                    # print(j,i)
                    curr_val-=arr[i]
                    i+=1
                    j-=1
                elif curr_val>target:
                    curr_val-=arr[i]
                    i+=1
                    j-=1
                else:
                    curr_val+=arr[j]

                j+=1
        # print(ans)
        ans.sort()
        if len(ans)>=2:
            return ans[0]+ans[1]
        return -1




