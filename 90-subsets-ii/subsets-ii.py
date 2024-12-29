class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret: list[list[int]] = []
        visited = set()

        def dfs(current_work: list[int], current_i: int) -> None:
            ret.append(current_work)
            visited.add(tuple(current_work))

            for i in range(current_i, len(nums)):
                tmp = current_work[:] + [nums[i]]
                if tuple(tmp) not in visited:
                    dfs(tmp, i+1)

        dfs([], 0)

        return ret