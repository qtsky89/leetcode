class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        boat can carry two people same time

        example1.
            people = [1, 2] limit = 3

            boat (1, 2) => 1 boat

        example2
            people = [3, 2, 2, 1] limit = 3

            boat (3) (2, 1) (2) => 3 boat

        
            [1, 2, 2, 3]
             ^     ^

            people.sort()

            boat_count = 0
            if boat[i] + boat[j] > limit:
                boat_count += 1
                j -= 1
            else:
                boat_count += 1
                i, j = i+1, j-1

        '''
    
        people.sort()
        i, j = 0, len(people)-1

        boat_count = 0
        while i <= j:
            if people[i] + people[j] > limit:
                boat_count += 1
                j -= 1
            else:
                boat_count += 1
                i, j = i+1, j-1
        
        return boat_count
            