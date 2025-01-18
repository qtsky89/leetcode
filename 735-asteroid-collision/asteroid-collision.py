class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        asteroids = [5, 10, 15, -50]

                     

        '''

        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue

            # collide happen
            diff = -1
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] + asteroid

                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    break
                else:
                    stack.pop()
                    break
            
            if diff < 0:
                stack.append(asteroid)

        return stack