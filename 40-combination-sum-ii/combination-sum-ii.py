class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret: list[list[int]] = []

        candidates.sort()
        # cadndiates = 1 1 2 5 6 7 10
        #              ^ 

        def dfs(current_index: int, current_sum: int, current_work: list[int]) -> None:
            if current_sum == target:
                ret.append(current_work)
                return
            elif current_sum > target:
                return
            elif current_index == len(candidates):
                return
            
            for i in range(current_index, len(candidates)):
                if i > current_index and candidates[i] == candidates[i - 1]:
                    continue
                dfs(i+1, current_sum + candidates[i], current_work + [candidates[i]])
            
        dfs(0, 0, [])

        return ret