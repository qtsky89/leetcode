class Solution:
    ''' easy solution
    def isPalindrome(self, s: str) -> bool:
        ret = []
        for i in range(len(s)):
            if s[i].isalpha():
                ret.append(s[i].lower())
            elif s[i].isnumeric():
                ret.append(s[i])

        p1, p2 = 0, len(ret)-1
        while p1 < p2:
            if ret[p1] != ret[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1
        
        return True'''

    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s)-1

        while p1 < p2:
            a = s[p1].lower()
            b = s[p2].lower()

            if not a.isalnum():
                p1 += 1
                continue
            elif not b.isalnum():
                p2 -= 1
                continue
            elif a != b:
                return False
            
            p1 += 1
            p2 -= 1
        return True
                
                