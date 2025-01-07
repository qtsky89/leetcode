class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        example1.
            1, 2, 3, 4

            1, 2
            1, 3
            1, 4
            2, 3
            2, 4
            3, 4
        '''

        ret: list[list[int]] = []
        
        def dfs(current_index: int, current_work: list[int]) -> None:
            if len(current_work) == k:
                ret.append(current_work)
                return
            
            for i in range(current_index, n+1):
                dfs(i+1, current_work + [i])

        dfs(1, [])

        return ret
