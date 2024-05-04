class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        q = deque([[-1, []]])

        visited: set[tuple[int]] = set()
        ret = []
        while q:
            last_index, current_work = q.popleft()

            tmp_tuple = tuple(current_work)
            if tmp_tuple in visited:
                continue
            else:
                visited.add(tmp_tuple)

            tmp = sum(current_work)
            if tmp == target:
                ret.append(current_work)
            elif tmp > target:
                continue
            

            for i in range(last_index+1, len(candidates)):
                q.append([i, [*current_work, candidates[i]]])
        
        return ret