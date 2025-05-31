class TreeNode:
    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self.right=right


def inorder(head,stac,target):
    
    while head:                             
        stac.append(head)
        if head.val==target:
            return
        head=head.left
    while stac:
        node=stac.pop()
        node=node.right
        while node:
            stac.append(node)
            if node.val==target:
                return
            node=node.left
        

def findLCA(root,p,q):
    s1,s2=[],[]
    head=root
    inorder(head,s1,p)
    inorder(head,s2,q)
    sets1=set([])
    for i in s1:
        sets1.add(i.val)
    while s2:
        curr_val=s2.pop()
        if curr_val.val in sets1:
            return curr_val.val
    return root.val