class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        '''
        0 1 1 0 1 0
        ^
              ^   
                  ^


        visited => prevent duplicate work
        '''

        most_far = 0
        q = deque([0])

        while q:
            i = q.popleft()

            if i == len(s)-1:
                return True
            
            for next_index in range(max(i+minJump, most_far+1), min(i+maxJump+1, len(s))):

                if s[next_index] == '0':
                    q.append(next_index)

            most_far = max(most_far, i+maxJump)

        return False
        
            
