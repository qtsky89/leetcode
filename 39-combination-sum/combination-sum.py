class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret: list[list[int]] = []

        def dfs(current_index: int, current_sum: int, current_work: list[int]) -> None:
            if current_sum == target:
                ret.append(current_work[:])
                return
            elif current_sum > target:
                return
            elif current_index == len(candidates):
                return
            
            for i in range(current_index, len(candidates)):
                current_work.append(candidates[i])
                dfs(i, current_sum + candidates[i], current_work)
                current_work.pop()
            
        dfs(0, 0, [])

        return ret