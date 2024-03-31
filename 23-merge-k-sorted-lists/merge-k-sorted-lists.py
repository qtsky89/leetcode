# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        4 -> 5
        3 -> 4
        6

        1 -> 1 -> 2 -> 
        '''

        # make dummy node
        ret = ListNode(None)
        p = ret

        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, [lists[i].val, i])

        while heap:
            _, i = heapq.heappop(heap)

            p.next = lists[i]
            lists[i] = lists[i].next

            if lists[i]:
                heapq.heappush(heap, [lists[i].val, i])

            p = p.next

        return ret.next

        