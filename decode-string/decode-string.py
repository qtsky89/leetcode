class Solution:
    def decodeString(self, strs: str) -> str:
        ret = ''
        count_stack, alpha_stack = [], []
        
        i = 0
        while i < len(strs):
            if strs[i].isdigit():
                count = 0
                while strs[i].isdigit():
                    count = count * 10 + int(strs[i])
                    i += 1
                count_stack.append(count)
            elif strs[i] == '[':
                alpha_stack.append(ret)
                ret = ''
                i += 1
            elif strs[i] == ']':
                tmp = alpha_stack.pop()
                count = count_stack.pop()
                
                for _ in range(0, count):
                    tmp += ret
                ret = tmp
                i += 1
            else:
                ret += strs[i]
                i += 1
                
        return ret