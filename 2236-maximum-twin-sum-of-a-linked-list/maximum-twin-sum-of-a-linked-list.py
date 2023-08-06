# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        1.
        5 -> 4 -> 2-> 1

        case1 : 5 + 1
        case2 : 4 + 2

        max : 6

        2.
        4 -> 2 -> 2 -> 3

        case1 : 4 + 3
        case2 : 2 + 2

        max = 7
        '''

        tmp: list[int] = []

        p = head
        while p:
            tmp.append(p.val)
            p = p.next
        
        max_val = -float('inf')
        for i in range(len(tmp)//2):
            val = tmp[i] + tmp[-i-1]
            max_val = max(max_val, val)
        
        return max_val

        







