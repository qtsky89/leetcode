class Solution:
    def calculate(self, s: str) -> int:
        '''
        example1.
            s = 3 + 2 * 2
                        ^
            stack = 3, 4

            sum(stack) = 7

        example2.
            s = 3 / 2

            stack = 1

            sum(stack) = 1
        
        example3.
            s = 3 - 5 / 2

            stack = 3, -2

            sum(stack) = 1
        '''

        i = 0
        stack = []

        # time: O(N), space: O(N)
        while i <= len(s)-1:
            if s[i] == ' ' or s[i] == '+':
                i += 1
                continue

            if s[i] in '-*/':
                stack.append(s[i])
                i += 1
            elif s[i].isdigit():
                j = i
                while j <= len(s)-1 and s[j].isdigit():
                    j += 1
                tmp_num = int(s[i:j])

                if stack and stack[-1] == '-':
                    stack.pop()
                    stack.append(-tmp_num)
                elif stack and stack[-1] == '*':
                    stack.pop()
                    stack.append(stack.pop() * tmp_num)
                elif stack and stack[-1] == '/':
                    stack.pop()
                    stack.append(int(stack.pop() / tmp_num))
                else:
                    stack.append(tmp_num)
                i = j
        
        return sum(stack)

