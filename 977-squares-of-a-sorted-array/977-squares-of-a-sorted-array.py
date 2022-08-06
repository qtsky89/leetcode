class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        min_index = self.min_abs_index(nums)
        
        
        ret = []
        p1, p2 = min_index, min_index+1
        while p1 >= 0 and p2 <= len(nums)-1:
            if abs(nums[p1]) <= abs(nums[p2]):
                ret.append(nums[p1] ** 2)
                p1 -= 1
            else:
                ret.append(nums[p2] ** 2)
                p2 += 1
        
        while p1 >= 0:
            ret.append(nums[p1] ** 2) 
            p1 -= 1
        
        while p2 <= len(nums)-1:
            ret.append(nums[p2] ** 2)
            p2 += 1
        
        return ret        
                
        
        
    
    
    def min_abs_index(self, nums: List[int]) -> int:
        tmp = [abs(nums[i]) for i in range(len(nums))]
        min_val = min(tmp)
        return tmp.index(min_val)