class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [1, 2, 3]

        []
        [1]
        [2]
        [3]
        [12]  =>  [21]
        [23]
        [13]
        [123]
        '''

        nums.sort()

        ret: list[list[int]] = []

        # something here
        def dfs(current_work: list[int]) -> None:
            ret.append(current_work)

            for n in nums:
                if not current_work or (current_work and current_work[-1] < n):
                    dfs(current_work + [n])

        dfs([])

        return ret
        