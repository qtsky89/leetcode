class Solution:
    def removeDuplicates(self, strings: str, k: int) -> str:
        '''
        stack = [d, 1] [d, 2]

        d e e e d b b c c c b d a a 

        d d b b c c c b d a a
        '''

        # stack = [[d, 1] [d, 2]] ...
        stack: list[list[str, int]] = []

        for s in strings:
            if not stack:
                stack.append([s, 1])
                continue
            
            if stack[-1][0] == s:
                stack.append([s, stack[-1][1] + 1])
            else:
                stack.append([s, 1])
            
            if stack[-1][1] == k:
                for i in range(k):
                    stack.pop()

        return ''.join([char for char, count in stack])
