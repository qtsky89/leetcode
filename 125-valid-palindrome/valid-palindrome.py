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
        '''
        s = "Was it a car or a cat I saw?"
                          ^^


        '''

        p1, p2 = 0, len(s)-1
        while p1 <= p2:
            while p1 <= len(s)-1 and not s[p1].isalnum():
                p1 += 1
            
            while p2 >= 0 and not s[p2].isalnum():
                p2 -= 1
                        
            if p1<=p2 and s[p1].lower() != s[p2].lower():
                return False
            
            p1 += 1
            p2 -= 1
        
        return True
                
                