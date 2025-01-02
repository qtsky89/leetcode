# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode:
    def __init__(self, listNode: ListNode = None) -> None:
        self.node = listNode

    def __lt__(self, other: 'HeapNode') -> bool:
       return True 


from heapq import heappush, heapify


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        heap = [(1, Node), (2, Node), (2, Node)]

        '''
        heap = []
        
        for head in lists:
            if head:
                heap.append((head.val, HeapNode(head)))
        
        heapify(heap)

        dummy = ListNode()
        p = dummy
        
        while heap:
            node = heappop(heap)[1].node
            p.next = node
            p = p.next

            if node.next:
                heappush(heap, (node.next.val, HeapNode(node.next)))
        
        return dummy.next
        