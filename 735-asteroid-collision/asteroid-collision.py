class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        i = 0
        while i <= len(asteroids)-1:
            # collide
            a = asteroids[i]
            while stack and (stack[-1] > 0 and a < 0):
                diff = a + stack[-1]

                if diff == 0: # both collide
                    a = 0
                    stack.pop()
                elif diff < 0: # asteroids[i] win
                    stack.pop()
                elif diff > 0: # stack win
                    a = 0
            if a != 0:
                stack.append(a)

            i+=1
                  
        return stack
