class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        asteroids = [5, 10, -5]
        '''

        i = 0

        stack = []
        while i <= len(asteroids)-1:
            if not stack:
                stack.append(asteroids[i])
                i+=1
                continue
            
            if ((stack[-1] > 0 and asteroids[i] > 0) or
                (stack[-1] < 0 and asteroids[i] < 0) or
                (stack[-1] < 0 and asteroids[i] > 0)
            ):
                stack.append(asteroids[i])
                i += 1
                continue
            
            # collition
            if abs(stack[-1]) == abs(asteroids[i]):
                stack.pop()
                i += 1
                continue
            elif abs(stack[-1]) > abs(asteroids[i]):
                i += 1
                continue
            
            while stack and stack[-1] > 0 and asteroids[i] < 0 and abs(stack[-1]) < abs(asteroids[i]):
                stack.pop()
            
        return stack