class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []

        nums.sort()

        def dfs(current_work: list[int], visited: set[int]) -> None:
            if len(current_work) == len(nums):
                ret.append(current_work)
                return
            
            for i, n in enumerate(nums):
                if i-1 >= 0 and nums[i-1] == nums[i] and (i-1) in visited:
                    continue
                if i not in visited:
                    dfs(current_work + [n], visited | {i})
        
        dfs([], set())

        return ret