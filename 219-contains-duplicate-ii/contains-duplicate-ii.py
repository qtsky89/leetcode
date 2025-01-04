class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        nums = 1, 2, 3, 1, 2, 3      k=2
               ^     ^               set={1, 2, 3}  False
                   ^    ^            set={1, 2, 3}  False
                      ^    ^         set={1, 2, 3}  False
                         ^    ^      set={1, 2, 3}  False
        '''

        i, j = 0, min(k, len(nums)-1)
        visited = set()

        while j <= len(nums)-1:
            if i == 0:
                visited = set(nums[:j+1])
            else:
                visited.remove(nums[i-1])
                visited.add(nums[j])
            
            # there is duplicate
            if len(visited) != (j-i+1):
                return True
            
            i, j = i+1, j+1

        return False
                
            