class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        ret = [set(), set()]
        for i in range(len(nums1)):
            if nums1[i] not in nums2_set:
                ret[0].add(nums1[i])
            
        for j in range(len(nums2)):
            if nums2[j] not in nums1_set:
                ret[1].add(nums2[j])
        return ret