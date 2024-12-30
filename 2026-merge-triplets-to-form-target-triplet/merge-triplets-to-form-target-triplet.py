class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        '''

        2, 5, 3
        1, 7, 5

        2, 7, 5


        # fist step, remove triplet that have above target value
        # second stemp, 
            first element is in the triplet?
            second element is in the triplet?
            third element is in the triplet?

            it's all true then return True
            else False

        '''

        # fist step, remove triplet that have above target value
        filtered_triplets: list[list[int]] = []
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            else:
                filtered_triplets.append([x, y, z])
        
        '''
        # second step, 
        first element is in the triplet?
        second element is in the triplet?
        third element is in the triplet?

        it's all true then return True
        else False
        '''
        
        is_x, is_y, is_z = False, False, False

        for x, y, z in filtered_triplets:
            if x == target[0]:
                is_x = True
            if y == target[1]:
                is_y = True
            if z == target[2]:
                is_z = True
        
        return is_x and is_y and is_z
        