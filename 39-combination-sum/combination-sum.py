from collections import deque

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        inputs = []

        for i in range(len(candidates)):
            inputs.append([[candidates[i]], candidates[i]])
        
        # [[[2], 2], [[3], 3], [[6], 6], [[7], 7]]

        q = deque(inputs)

        ret = []
        while q:
            # item = [2]
            item, total = q.popleft()

            if total == target:
                ret.append(item)
                continue
            elif total > target:
                continue
            
            for i in range(len(candidates)):
                if candidates[i] >= item[-1]:
                    if total + candidates[i] <= target:
                        q.append([ [*item, candidates[i]], total + candidates[i] ])
        return ret
            
            