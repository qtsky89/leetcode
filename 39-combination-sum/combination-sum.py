class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # [2, 3, 6, 7]
        ret: list[list[int]] = []
        def dfs(current_work: list[int], current_sum: int, current_index: int) -> None:
            if current_sum == target:
                ret.append(current_work)
                return
            
            for i in range(current_index, len(candidates)):
                if current_sum + candidates[i] <= target:
                    dfs(current_work + [candidates[i]], current_sum + candidates[i], i)
                
        dfs([], 0, 0)


        return ret
        