class Solution:
    def decodeString(self, s: str) -> str:
        current_str = ''
        number_stack, alpha_stack = [], []

        i = 0
        while i <= len(s) - 1 :
            if s[i].isdigit():
                j = i
                while j+1 <= len(s)-1 and s[j+1].isdigit():
                    j+=1
                number = int(s[i:j+1])
                number_stack.append(number)
                i = j+1
            elif s[i] == '[':
                alpha_stack.append(current_str)
                current_str = ''
                i += 1
            elif s[i] == ']':
                tmp = ''
                for j in range(number_stack.pop() ):
                    tmp += current_str
                current_str = alpha_stack.pop() + tmp
                i+=1
            else:
                current_str += s[i]
                i += 1
        return current_str