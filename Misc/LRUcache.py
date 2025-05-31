
class Node:
    def __init__(self,value :int):
        self.value=value
        self.lnode=None
        self.rnode=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.key_value={}
        self.counter=0
        self.head=None
        self.tail=None

    def get(self, key: int) -> int:
        if key in self.key_value:
            self.remove_from_queue(self.key_value[key][1])
            self.insert_node_in_queue(self.key_value[key][1])
            return self.key_value[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.key_value:
            if self.counter==self.capacity:
                val=self.head.value
                self.pop_from_queue()
                self.counter-=1
                self.key_value.pop(val)
            new_node=Node(key)
            self.insert_node_in_queue(new_node)
            self.key_value[key]=[value,new_node]
            self.counter+=1

        else:
            self.remove_from_queue(self.key_value[key][1])
            self.insert_node_in_queue(self.key_value[key][1])
            self.key_value[key][0]=value
       
    def insert_node_in_queue(self,new_node : Node):
        if self.head==None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.rnode=new_node
            new_node.lnode=self.tail
            new_node.rnode=None
            self.tail=new_node
    
    def pop_from_queue(self):
        self.head=self.head.rnode
    def remove_from_queue(self,node : Node):
        if self.head==self.tail:
            return
        elif node==self.head:
            # print(node.rnode.value)
            node.lnode=None
            self.head=node.rnode
            node.rnode.lnode=None
        elif self.tail==node:
            self.tail=self.tail.lnode
            node.lnode.rnode=None
            node.lnode=None
        else:
            node.lnode.rnode=node.rnode
            node.rnode.lnode=node.lnode
            node.lnode,node.rnode=None,None
        
        



if __name__=="__main__":
    # lis=["LRUCache","put","put","get","put","put","get"]
    # inp=[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    lis=["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]

    inp= [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    for i in range(len(lis)):
        if lis[i]=="LRUCache":
            obj =LRUCache(inp[i][0])
        elif lis[i]=="get":
            print(obj.get(inp[i][0]))
        else:
            print(obj.put(inp[i][0],inp[i][1])) 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)