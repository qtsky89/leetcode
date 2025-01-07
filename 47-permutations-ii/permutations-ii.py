class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [1, 1, 2]

        output = [1, 1, 2] [1, 2, 1] [2, 1, 1]
        '''

        nums.sort()

        ret: list[list[int]] = []

        def dfs(current_work: list[int], visited: set[int]) -> None:
            # ending condition
            if len(current_work) == len(nums):
                ret.append(current_work)
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and i-1 in visited:
                    continue
                if i not in visited:
                    dfs(current_work + [nums[i]], visited | {i})
        dfs([], set())

        return ret

        