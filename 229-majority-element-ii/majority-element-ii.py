class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)

        '''
        nums = [3, 2, 3]

        c = {
            2 : 1
            3 : 2
        }


        '''

        ret =  []

        for key, value in c.items():
            if value > (len(nums) // 3):
                ret.append(key)
        
        return ret