"""Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.
Input:
N = 9, K = 3
arr[] = 1 2 3 1 4 5 2 3 6
Output: 
3 3 4 5 5 5 6 
Explanation: 
1st contiguous subarray = {1 2 3} Max = 3
2nd contiguous subarray = {2 3 1} Max = 3
3rd contiguous subarray = {3 1 4} Max = 4
4th contiguous subarray = {1 4 5} Max = 5
5th contiguous subarray = {4 5 2} Max = 5
6th contiguous subarray = {5 2 3} Max = 5
7th contiguous subarray = {2 3 6} Max = 6

1,4,2,-1,-10
4 5 6
"""



# def get_sol(arr,k):
#     len_arr=len(arr)
#     k_arr=[]
#     for i in range(k):
#         k_arr.append(arr[i])
#     i,j=0,k
#     ans=[]
#     while j<len_arr:
#         ans.append(max(k_arr))
#         k_arr.remove(arr[i])
#         i+=1
#         k_arr.append(arr[j])
#         j+=1
#     ans.append(max(k_arr))
#     print(ans)
# if __name__=="__main__":
#     get_sol([1,2,3,1,4,5,2,3,6],3)



"""Q. Given an array of distinct n integers. The task is to check whether reversing one sub-array make the array sorted or not. If the array is already sorted or by reversing a subarray once makes it sorted, print "Yes", else print "No".

Input : arr [] = {1, 2, 5, 4, 3}
Output : Yes
By reversing the subarray {5, 4, 3}, 
the array will be sorted.

Input : arr [] = { 1, 2, 4, 5, 3 }
Output : No

Input : arr [] = {1, 2, 5, 4, 3, 6, 7, 8}
Output : Yes

Input : arr [] = {1, 2, 5, 4, 3, 8, 7, 6}
Output : No
"""
def sol(arr):
    len_arr=len(arr)
    for i in range(1,len_arr):
        if arr[i]<arr[i-1]:
            break
    if i==len_arr-1:
        return "Yes"
    for j in range(i,len_arr):
        if arr[j]>arr[j-1]:
            break
    print(j)
    if j==len_arr-1:
        return "Yes"
    curr_arr=arr[i-1:j]
    curr_arr=curr_arr[::-1]
    ar=arr[:i-1]+curr_arr+arr[j:]
    print(ar)
    for i in range(1,len_arr):
        if ar[i]<ar[i-1]:
            return "No"
    return "Yes"


if __name__=="__main__":
    print(sol([1, 2, 5, 4, 3, 6, 7, 8]))