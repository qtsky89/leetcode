class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        '''
        nums[i] + nums[j] + nums[k] => 
        
        -4 -1 -1 0 1 2
        ^   ^        ^
        '''

        ret = []
        visited = set()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1

            while j < k :
                if nums[i] + nums[j] + nums[k] == 0:
                    key  = (nums[i], nums[j], nums[k])

                    if key not in visited:
                        ret.append([nums[i], nums[j], nums[k]])
                    visited.add(key)
                    
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return ret