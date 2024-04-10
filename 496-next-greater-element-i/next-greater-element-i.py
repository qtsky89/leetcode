class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        nums1 = 4 1 2
                -1 3 -1


        nums2 = 1 3 4 2
                
        {
            1 : 3
            3 : 4
        }

        stack = 4 2



                

        nums1 = 2, 4
        nums2 = 1, 2, 3, 4

        {
            1 : 2
            2 : 3
            3:  4

        }

        stack = 4

        '''

        dic = {}
        stack = []

        for n in nums2:    
            while stack and stack[-1] < n:
                item = stack.pop()
                dic[item] = n
            stack.append(n)
        
        ret = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            if n in dic:
                ret[i] = dic[n]
        return ret
