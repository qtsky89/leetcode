class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        + - => explode recursively

        asteroids = 5, 10 -5
                           ^

        stack = 5 10
        '''

        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
                continue

            # explode
            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a

                # new one will be explode
                if diff > 0:
                    a = 0
                elif diff < 0:
                    stack.pop()
                else:
                    stack.pop()
                    a = 0
            
            if a != 0:
                stack.append(a)
        return stack


                
            