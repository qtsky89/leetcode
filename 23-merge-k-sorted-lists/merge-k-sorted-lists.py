# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        [
        1->4->5,
        1->3->4,
        2->6
        ]
        '''

        ret = ListNode(None)
        p = ret

        # 1, 1, 2
        heap = []
        for index, l in enumerate(lists):
            if l:
                heapq.heappush(heap, [l.val, index])
        
        while heap:
            small_val, index = heapq.heappop(heap)
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(heap, [lists[index].val, index])

            p.next = ListNode(small_val)
            p = p.next

        return ret.next