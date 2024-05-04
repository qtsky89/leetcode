from collections import deque

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_set = set(nums)

        ret = []

        q = deque([[]])

        while q:
            item = q.popleft()

            if len(item) == len(nums):
                ret.append(list(item))
                continue
            
            for new_num in (nums_set - set(item)):
                q.append([*item, new_num])
        
        return ret