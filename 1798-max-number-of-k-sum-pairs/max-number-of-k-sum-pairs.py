class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        '''
        nums = [ 1, 2, 3, 4 ] k = 5
                 ^        ^
               [ 2, 3 ]
               
               []
                    max_operation => 2
        
        nums = [ 1, 3, 3, 3, 4 ] k = 6
                 ^           ^
                    ^        ^
                    ^      ^         count += 1
                       ^^              
        '''

        nums.sort()

        count = 0
        p1, p2 = 0, len(nums)-1

        while p1 < p2:
            tmp = nums[p1] + nums[p2]
            if tmp == k:
                count += 1
                p1, p2 = p1+1, p2-1
            elif tmp > k:
                p2 -= 1
            else:
                p1 += 1
        return count
        