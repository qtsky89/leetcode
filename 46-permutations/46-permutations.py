class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def dfs(current_work: List[int], visited: set):
            if len(current_work) == len(nums):
                ret.append(current_work)
                return
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    new_current_work = current_work + [nums[i]]
                    new_visited = visited | {nums[i]}
                    dfs(new_current_work, new_visited)
            
        dfs([], set())
        
        return ret