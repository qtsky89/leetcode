class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        '''
        Input: nums1 = [1,2,3], nums2 = [2,4,6]

            return [[nums1 - num2] [nums2 - nums1]]
        Output: [[1,3],[4,6]]
        '''
        
        set1, set2 = set(nums1), set(nums2)
        return [list(set1-set2),list(set2-set1)]