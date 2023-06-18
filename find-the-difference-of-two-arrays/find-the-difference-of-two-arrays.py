class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        ret1, ret2 = set(), set()
        for i in range(len(nums1)):
            if nums1[i] not in nums2_set:
                ret1.add(nums1[i])

        for i in range(len(nums2)):
            if nums2[i] not in nums1_set:
                ret2.add(nums2[i])

        return [list(ret1), list(ret2)]

        