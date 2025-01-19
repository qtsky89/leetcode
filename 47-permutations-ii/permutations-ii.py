class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        def dfs(current_work: list[int], visited: set[int]) -> None:
            if len(current_work) == len(nums):
                ret.append(current_work[:])
                return
            
            for i in range(len(nums)):
                if i-1>=0 and nums[i-1] == nums[i] and i-1 in visited:
                    continue

                if i not in visited:
                    visited.add(i)
                    current_work.append(nums[i])

                    dfs(current_work, visited)

                    current_work.pop()
                    visited.remove(i)
        
        dfs([], set())

        return ret