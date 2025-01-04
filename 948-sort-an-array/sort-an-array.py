class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        m = len(nums) //2

        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])

        return self.merge(left, right)
    
    def merge(self, left_arr: list[int], right_arr: list[int]) -> list[int]:
        i, j = 0, 0

        ret = []

        while i <= len(left_arr)-1 and j <= len(right_arr)-1:
            if left_arr[i] <= right_arr[j]:
                ret.append(left_arr[i])
                i += 1
            else:
                ret.append(right_arr[j])
                j += 1
        
        while i <= len(left_arr)-1:
            ret.append(left_arr[i])
            i += 1

        while j <= len(right_arr)-1:
            ret.append(right_arr[j])
            j += 1
    
        return ret