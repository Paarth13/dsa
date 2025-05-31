from heapq import heappush,heappop,heapify
def running_median(A):
        max_heap,min_heap=[],[]
        heapify(max_heap),heapify(min_heap)
        median=9**10
        len_max_heap,len_min_heap=0,0
        for i in A:
            if i<median:
                if len_max_heap>len_min_heap:
                    heappush(min_heap,-heappop(max_heap))
                heappush(max_heap,-i)
            elif i>median:
                if len_max_heap<len_min_heap:
                    heappush(max_heap,-heappop(min_heap))
                heappush(min_heap,i)
            else:
                return True
            len_max_heap,len_min_heap=len(max_heap),len(min_heap)
            if len_max_heap==len_min_heap:
                median=((-max_heap[0])+min_heap[0])/2
            elif len_max_heap<len_min_heap:
                    
                    median=min_heap[0]
            else:
                median=-max_heap[0]
        return False
if __name__=="__main__":
    running_median([ -2147483648, 2147483647, 5, 1000005, -10023326 ])
