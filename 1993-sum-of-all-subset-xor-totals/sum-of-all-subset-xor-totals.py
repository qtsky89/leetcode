class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        def dfs(current_index: int, current_work: list[int]) -> None:
            nonlocal total
            tmp = 0
            for work in current_work:
                tmp ^= work
            total += tmp

            for i in range(current_index, len(nums)):
                dfs(i+1, current_work + [nums[i]] )

        dfs(0, [])

        return total