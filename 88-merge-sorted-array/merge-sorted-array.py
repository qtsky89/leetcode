class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        '''
        nums1 = [1, 2, 3, 0, 0, 0]
                       ^        ^

        nums2 = [2, 5, 6]
                       ^
        '''

        i, j, k = m-1, n-1, len(nums1)-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i, k = i-1, k-1
            else:
                nums1[k] = nums2[j]
                j, k = j-1, k-1
        
        while i >= 0:
            nums1[k] = nums1[i]
            i, k = i-1, k-1
        
        while j>=0:
            nums1[k] = nums2[j]
            j, k = j-1, k-1

        