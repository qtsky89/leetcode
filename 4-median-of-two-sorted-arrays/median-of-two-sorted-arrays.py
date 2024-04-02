class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ret = [0] * (len(nums1) + len(nums2))

        p1, p2, p3 = 0, 0, 0
        while p1 <= len(nums1)-1 and p2 <= len(nums2)-1:
            if nums1[p1] < nums2[p2]:
                ret[p3] = nums1[p1]
                p1, p3 = p1+1, p3+1
            else:
                ret[p3] = nums2[p2]
                p2, p3 = p2+1, p3+1
        
        while p1 <= len(nums1)-1:
            ret[p3] = nums1[p1]
            p1, p3 = p1+1, p3+1

        while p2 <= len(nums2)-1:
            ret[p3] = nums2[p2]
            p2, p3 = p2+1, p3+1
        
        # odd length
        if len(ret) % 2 != 0:
            return ret[len(ret)//2]
        else: # 4    
            return (ret[len(ret)//2] + ret[len(ret)//2-1]) / 2

        