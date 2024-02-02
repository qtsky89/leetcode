class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
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
                    else:
                        p1 += 1
            count = max(count, p2-p1)
        return count