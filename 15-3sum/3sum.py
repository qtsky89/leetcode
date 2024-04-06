class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        '''

        -4 -1 -1 0 1 2
         ^  
        

        '''

        ret = []
        visited = set()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1

            while j < k:
                tmp = nums[j] + nums[k]

                # bingo
                if tmp == -nums[i]:
                    key = ','.join([str(nums[i]), str(nums[j]), str(nums[k])])
                    if  key not in visited:
                        ret.append([nums[i], nums[j], nums[k]])
                        visited.add(key)
                    j += 1
                    k -= 1
                elif tmp > -nums[i]:
                    k -= 1
                else:
                    j += 1
        return ret

                