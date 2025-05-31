class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
head,tail=None,None

def create_ll_from_list(arr):
    global head,tail
    for i in arr:
        if not head:
            head=Node(i)
            tail=head
        else:
            tail.next=Node(i)
            tail=tail.next


def rev_ll(od,start,end):
    global head,tail
    stc=[]
    poi=start
    while poi!=end:
        stc.append(poi)
        poi=poi.next
    poi=stc.pop()
    od.next=poi
    while stc:
        poi.next=stc.pop()
        poi=poi.next
    poi.next=end
    

def solve():
    global head,tail
    ptr=head
    ptr1=ptr
    od=ptr
    f=0
    while ptr:
        if ptr.val%2!=0:
            if f==1:
                rev_ll(od,ptr1,ptr)
                ptr1=ptr
                f=0
            od=ptr
        else:
            if f==0:
                ptr1=ptr
                f=1
        ptr=ptr.next
def print_ll():
    global head
    pointr=head
    while pointr:
        print(pointr.val)
        pointr=pointr.next
def main():
    # num=int(input())
    # x=input().split(" ")
    # arr=list(map(int,x))
    # print(arr)
    create_ll_from_list([2,4,6,1])
    print_ll()
    solve()
    print_ll()


if __name__=="__main__":
    main()