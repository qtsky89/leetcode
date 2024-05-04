class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        []
        [1]
        [2]
        [1, 2]
        [2, 2]
        [1, 2, 2]
        '''

        nums.sort()

        ret: list[list[int]] = []
        visited = set()

        q = deque([[-1, []]])

        while q:
            index, item = q.popleft()
            tmp_tuple = tuple(item)
            if tmp_tuple in visited:
                continue
            else:
                visited.add(tmp_tuple)

            ret.append(item)

            for i in  range(index+1, len(nums)):
                q.append([i, (*item, nums[i])])
        
        return list(ret)
            

            

        

