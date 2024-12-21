from collections import deque

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        nums = 1, 2, 3, 4
                1, 4 => 5
        
        nums = 1, 2, 3, 4, 5 

            


        I need to choose some value. And sum of that values sould be sum(nums) // 2
        '''

        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False
        
        visited = set()
        q = deque([(0, 0)])

        while q:
            index, cur_sum = q.popleft()
            if (index, cur_sum) in visited:
                continue
            visited.add((index, cur_sum))

            if cur_sum == total_sum // 2:
                return True
            elif cur_sum > total_sum:
                continue
            elif index == len(nums):
                continue
            
            q.append((index+1, cur_sum))
            q.append((index+1, cur_sum + nums[index]))
        
        return False