class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        '''
        arr = [1, 2, 2, 1, 1, 3]

            1 : 3
            2 : 2
            3 : 1  return True

        arr = [1,2]
           
            1 : 1
            2 : 1
                  return False
        '''

        c = Counter(arr)
        
        visited = set()

        for v in c.values():
            if v in visited:
                return False
            else:
                visited.add(v)
        
        return True


