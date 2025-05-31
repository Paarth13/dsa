def find_subs(A,lena,curr_index,curr_arr,subs):
    if lena==curr_index:
        val=tuple(curr_arr.copy())
        if val not in subs:
            subs.add(val)
        return
    find_subs(A,lena,curr_index+1,curr_arr,subs)
    curr_arr.append(A[curr_index])
    find_subs(A,lena,curr_index+1,curr_arr,subs)
    curr_arr.remove(A[curr_index])
    return

def main():
    listOfNums=[1,2,2]
    subs=set()
    find_subs(listOfNums,len(listOfNums),0,[],subs)
    subs=sorted(subs)
    print(subs)
if __name__=="__main__":
    main()