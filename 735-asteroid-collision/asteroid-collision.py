class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        asteroids = [5, 10, 15, -5, -5, -25, 30]
                                         ^       
        
        stack = [-25, 30]
        '''

        stack = []
        
        i = 0
        while i<= len(asteroids)-1:
            if not stack or asteroids[i] > 0:
                stack.append(asteroids[i])
                i+=1
                continue

            if (asteroids[i] < 0 and stack[-1] > 0) and (stack[-1] + asteroids[i]) > 0:
                i+=1
                continue
            elif (asteroids[i] < 0 and stack[-1] > 0) and (stack[-1] + asteroids[i]) == 0:
                stack.pop()
                i+=1
                continue
            elif (asteroids[i] < 0 and stack[-1] > 0) and (stack[-1] + asteroids[i]) < 0:
                while stack and (asteroids[i] < 0 and stack[-1] > 0) and (stack[-1] + asteroids[i]) < 0:
                    stack.pop()
            else:
                stack.append(asteroids[i])
                i+=1
        return stack
                   