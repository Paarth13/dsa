class Node:
    def __init__(self,val) -> None:
        self.val=val
        self.next=None
head=None
tail=None
def create_ll(num):
    global head,tail
    while num:
        if not head:
            head=Node(int(input("Please Enter number")))
            tail=head
        else:
            tail.next=Node(int(input("Please Enter number")))
            tail=tail.next
        num-=1

def create_ll_from_list(arr):
    global head,tail
    for i in arr:
        if not head:
            head=Node(i)
            tail=head
        else:
            tail.next=Node(i)
            tail=tail.next

def print_ll():
    global head
    pointr=head
    while pointr:
        print(pointr.val)
        pointr=pointr.next

def rev_list():
    global head,tail
    pointr=head
    stc=[]
    while pointr:
        stc.append(pointr)
        pointr=pointr.next
    pointr=stc.pop()
    head=pointr
    while stc:
        pointr.next=stc.pop()
        pointr=pointr.next
    tail=pointr
    pointr.next=None
    
def main():
    # num=5
    # create_ll(num)
    create_ll_from_list([1,2,3,])
    print_ll()
    rev_list()
    print()
    print_ll()
    create_ll_from_list([10,12,13])
    print()
    print_ll()
if __name__=="__main__":
    main()