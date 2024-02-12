class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''

        '''

        tmp = []

        for i in range(len(s)):
            if s[i].isalpha():
                tmp.append(s[i].lower())
            elif s[i].isnumeric():
                tmp.append(s[i])
        
        i, j = 0, len(tmp)-1

        while i <= j:
            if tmp[i] != tmp[j]:
                return False
            i+=1
            j-=1
        return True
            


        