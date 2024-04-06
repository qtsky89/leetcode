class Solution:
    def minRemoveToMakeValid(self, strings: str) -> str:
        ret = []
        open_count = 0

        for s in strings:
            if s == '(':
                open_count += 1
                ret.append(s)
            elif s == ')' and open_count > 0:
                open_count -= 1
                ret.append(s)
            elif s != ')':
                ret.append(s)
        
        filtered = deque()
        for i in range(len(ret)-1, -1, -1):
            if ret[i] == '(' and open_count > 0:
                open_count -= 1
                continue
            else:
                filtered.appendleft(ret[i])
        
        return ''.join(filtered)