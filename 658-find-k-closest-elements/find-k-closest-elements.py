from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        arr = 2, 4, 6, 9, 10          x = 8, k = 4 
                       ^


        '''

        # find right index to start

        l, r = 0, len(arr)-1

        while l <= r:
            m = l + (r-l) // 2

            if arr[m] == x:
                r = m -1
            elif arr[m] > x:
                r = m - 1
            else:
                l = m + 1
            
        # l will pointing the insert index
        # compare l, l-1 find root
        
        if l > len(arr)-1:
            l -= 1
        elif l-1 >= 0 and abs(arr[l-1] - x) <= abs(arr[l] - x):
            l -= 1
        
            
        # q = [(left_index, right_index)]
        q = deque([(l, l)])
        
        while q:
            i, j = q.popleft()

            if j - i + 1 == k:
                return arr[i:j+1]
            
            if i-1 >= 0 and j+1 <= len(arr)-1:
                if abs(x - arr[i-1]) <= abs(x - arr[j+1]):
                    q.append((i-1, j))
                else:
                    q.append((i, j+1))
            elif i-1 >= 0:
                q.append((i-1, j))
            elif j + 1 <= len(arr)-1:
                q.append((i, j+1))
        
            