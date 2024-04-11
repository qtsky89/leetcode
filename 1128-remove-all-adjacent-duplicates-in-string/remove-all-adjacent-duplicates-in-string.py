class Solution:
    def removeDuplicates(self, strings: str) -> str:
        stack = []

        for s in strings:
            if not stack:
                stack.append(s)
                continue
            
            if stack and stack[-1] == s:
                stack.pop()
                continue
            stack.append(s)
        
        return ''.join(stack)
            