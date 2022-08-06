from collections import Counter

class Solution:
    # nums1 = [1,2,2,1] nums2 = [2,2]
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # nums1_counter = {1:2, 2:2}
        nums1_counter = Counter(nums1)
        
        # nums2_counter = {2:2}
        nums2_counter = Counter(nums2)
        
        # unique_keys = {2}
        unique_keys = set(nums1_counter.keys()) & set(nums2_counter.keys())
        
        ret = []
        for key in unique_keys:
            # key = 2
            count = min(nums1_counter[key], nums2_counter[key])
            
            ret.extend([key] * count)
        
        return ret
        
        
        
        
        
        
        
        
        
        
        