class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''
            [2, 5, 3]
            [1, 7, 5]

            [2, 7, 5]
             ^  ^  ^


            [3, 2, 5]


            [2, 5, 3]
            [2, 3, 4]
            [1, 2, 5]
            [5, 2, 3]
             ^  ^  ^

            [5, 5, 5]

        '''

        # step1 remove tirplets that have bigger value than target
        filtered_triplets = []

        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            filtered_triplets.append([a, b, c])

        # step2 check the max value
        is_a, is_b, is_c = False, False, False
        for a, b, c in filtered_triplets:
            if a == target[0]:
                is_a = True
            if b == target[1]:
                is_b = True
            if c == target[2]:
                is_c = True
        
        return is_a and is_b and is_c
        
        

