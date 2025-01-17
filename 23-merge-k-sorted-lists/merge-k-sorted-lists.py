# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode:
    def __init__(self, node: ListNode) -> None:
        self.node = node

    def __lt__(self, other: 'HeapNode') -> bool:
        return True


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for li in lists:
            if li:
                heap.append((li.val, HeapNode(li)))
        
        heapq.heapify(heap)
    
        dummy = ListNode()
        p = dummy

        while heap:
            _, heap_node = heapq.heappop(heap)

            p.next = heap_node.node
            p = p.next

            node = heap_node.node.next

            if node != None:
                heapq.heappush(heap, (node.val, HeapNode(node)))
            

        return dummy.next