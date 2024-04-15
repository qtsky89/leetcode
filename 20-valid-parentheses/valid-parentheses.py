class Solution:
    def isValid(self, strings: str) -> bool:
        stack = []

        for s in strings:
            if s in '({[':
                stack.append(s)
                continue
            
            if s == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif s == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif s == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
