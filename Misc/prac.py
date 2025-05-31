# write your code here...
class Node:
    def __init__(self,x):
        self.val=x
        self.next=None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,val):
        if self.head==None:
            self.head=Node(val)
        else:
            c=self.head
            while c.next:
                c=c.next
            c.next=Node(val)
    def display(self):
        ans=[]
        c=self.head
        while c:
            ans.append(c.val)
            c=c.next
        # c.next=Node(val)
        print(ans)
    def returnHead(self):
        return self.head
def newListHead(A):
    first = A
    if not A or A.next == None:
        return A
    prev=None  
    startEve,second=A.next,A.next
    while(first and first.next and second and second.next):
        prev=first
        first.next=first.next.next
        second.next=second.next.next
        first,second=first.next,second.next
    while(first and first.next):
        prev=first
        first.next=first.next.next
        first=first.next
    while(second and second.next):
        second.next=second.next.next
        second=second.next
    if first:
        first.next=startEve
    else:
        prev.next=startEve
def main():
    ll = LinkedList()
    l = []
    for elem in l:
        ll.append(elem)
    ll.display()
    newListHead(ll.returnHead())
    ll.display()

if __name__=="__main__":
    main()
'''
3,1,5,7,9,12

3,5,9,1,7,12
'''
