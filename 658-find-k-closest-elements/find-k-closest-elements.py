from bisect import bisect_left
from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        arr = 1  2  3  4  5    k=4   x=3
                 a  x     b

                i=2, j=2
                i=1, j=3
        
        '''

        if len(arr) == 1:
            return arr

        index = bisect_right(arr, x)-1
        if index+1 <= len(arr)-1 and abs(x-arr[index]) > abs(x-arr[index+1]):
            index += 1

        q = deque([(index, index)])

        while q:
            i, j = q.popleft()

            if j-i+1 == k:
                return arr[i:j+1]
            
            if i-1 >= 0 and j+1 <= len(arr)-1:
                if abs(x - arr[i-1]) <= abs(x - arr[j+1]):
                    q.append((i-1, j))
                else:
                    q.append((i, j+1))
            elif i-1 >= 0:
                q.append((i-1, j))
            else:
                q.append((i, j+1))
        
        


        
        
        