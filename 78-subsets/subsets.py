class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret: list[list[int]] = []
        def dfs(current_work: list[int], current_i: int) -> None:
            ret.append(current_work)

            for i in range(current_i, len(nums)):
                dfs(current_work[:] + [nums[i]], i+1)

        dfs([], 0)

        return ret