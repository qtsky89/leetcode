class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [-4  -1  -1  0  1  2]
                i    j            k => 4 add result
                     i   j        k
                            i   j  k
        '''

        nums.sort()

        ret = []
        visited = set()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1

            # nums[j] + nums[k] == -nums[i] (should be)
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    if (nums[i], nums[j], nums[k]) not in visited:
                        ret.append([nums[i], nums[j], nums[k]])
                        visited.add((nums[i], nums[j], nums[k]))
                    j, k = j + 1, k - 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else:
                    j += 1
     
        return ret