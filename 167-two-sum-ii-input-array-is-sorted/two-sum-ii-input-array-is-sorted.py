class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''

        numbers = [2, 7, 11, 15]
                   ^          ^    17
                   ^      ^        13
                   ^   ^            9
        '''

        p1, p2 = 0, len(numbers)-1

        while p1 < p2:
            tmp = numbers[p1] + numbers[p2]
            
            if tmp == target:
                return [p1+1, p2+1]
            elif tmp > target:
                p2 -= 1
            else:
                p1 += 1
        
                