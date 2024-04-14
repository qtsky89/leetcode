class Solution:
    def removeDuplicates(self, strings: str, k: int) -> str:
        '''
        s = d e e e d b b c c c b d a a 
                    ^

        k = 3
        stack = [[d,1], [d, 1], [b, 1], [b, 2] ...]

        '''

        stack = []
        for s in strings:
            if stack and stack[-1][0] == s:
                stack.append([s, stack[-1][1]+1])
            else:
                stack.append([s, 1])
            
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()

        return ''.join([st[0] for st in stack ])