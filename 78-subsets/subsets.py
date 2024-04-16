from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [1, 2, 3]
        '''

        q = deque([[]])

        ret = []
        while q:
            item = q.popleft()
            
            ret.append(item)

            for n in nums:
                if not item:
                    q.append(item + [n])
                elif item[-1] < n:
                    q.append(item + [n])
        return ret
                    