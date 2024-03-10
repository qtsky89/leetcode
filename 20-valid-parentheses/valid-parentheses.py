class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            match s[i]:
                case '(' | '[' | '{':
                    stack.append(s[i])
                case ')':
                    if not stack or stack[-1] != '(':
                        return False
                    stack.pop()
                case ']':
                    if not stack or stack[-1] != '[':
                        return False
                    stack.pop()
                case '}':
                    if not stack or stack[-1] != '{':
                        return False
                    stack.pop()
        return len(stack) == 0
                    
                    
                