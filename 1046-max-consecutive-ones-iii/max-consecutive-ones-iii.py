class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ''' original k = 2
        nums = [0 0 0 1] k=4
                
                ^ ^

    1. count = 0   k= 4 -> 3

        '''

        p1, p2 = 0, 0
        count = 0
        while p2 <= len(nums)-1:
            if nums[p2] == 1:
                p2 += 1
            else:
                if k > 0:
                    k -= 1
                    p2 += 1
                else:
                    if nums[p1] == 0:
                        k += 1
                    p1 += 1
                    
            count = max(count, p2 - p1)

        return count






        