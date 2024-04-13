from collections import deque

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q = deque([[]])

        ret = []
        while q:
            visited = q.popleft()

            ret.append(visited)

            if len(visited) == len(nums):
                break

            for n in nums:
                if not visited or max(visited) < n:
                    q.append([*visited, n])
        
        return ret

            