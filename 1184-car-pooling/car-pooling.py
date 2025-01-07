class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        example1.
            trips = [[2,1,5], [3,3,7]], capacity = 4
                        ^         
            2
            1  2  3  4  5  6  7
            ^           ^

                  3=>2 1 passenger left in 3
            1  2  3  4  5  6  7
                  ^           ^

            return False

            1  2  3  4  5  6  7
            ^
        
        '''


        # trips = [[2,1,5], [3,3,7]]
        trips.sort(key = lambda x:x[1])

        # heap
        heap = []

        for num_passenger, start, end in trips:
            # TODO. add more capacity in current_capacity
            while heap and heap[0][0] <= start:
                _, num_drop_passenger = heapq.heappop(heap)
                capacity += num_drop_passenger

            if capacity < num_passenger:
                return False

            # 4 - 2 => 2
            capacity -= num_passenger

            # add 5 to the heap
            heapq.heappush(heap, (end, num_passenger))
        return True