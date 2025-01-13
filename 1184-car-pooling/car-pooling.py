class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        [2, 1, 5] [3, 3, 7]
                      ^

        heap = [(5, 2)]
                 ^  ^
        destination, passnger
        '''

        # sort by from
        trips.sort(key=lambda x:x[1])

        '''
        (5, 2)
         ^  ^
        to_i, passenger
        '''
        heap = []

        for passenger, from_i, to_i in trips:
            # heap process
            # heap[0][0] => to_i
            while heap and heap[0][0] <= from_i:
                tmp_to, tmp_passenger =  heapq.heappop(heap)
                capacity += tmp_passenger

            # don't have enough capacity        
            if capacity < passenger:
                return False
            
            capacity -= passenger

            heapq.heappush(heap, (to_i, passenger))
        
        return True



