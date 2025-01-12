from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the insert index using binary search
        index = bisect_left(arr, x)-1

        if index < 0:
            index = 0

        if index+1 <= len(arr)-1 and (abs(x-arr[index]) > abs(x-arr[index+1])):
            index += 1

        # start, end
        q = deque([(index, index)])
        
        while q:
            i, j = q.popleft()
            
            if j-i+1 == k:
                return arr[i:j+1]
            
            # left expand
            if (j+1 <= len(arr)-1 and i-1 >=0):
                if abs(arr[i-1] - x) <= abs(arr[j+1]-x):
                    q.append((i-1, j))
                else:
                    q.append((i, j+1))
            elif i-1 >=0:
                q.append((i-1, j))
            else:
                q.append((i, j+1))

            

        
        

        


        

        