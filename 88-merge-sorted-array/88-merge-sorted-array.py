class Solution:
    # TODO: try O(M+N) time complexity
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[m:m+n+1] = nums2
        
        nums1.sort()