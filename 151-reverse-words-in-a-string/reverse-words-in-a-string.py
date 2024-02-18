class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')

        ret = []
        for string in s_list:
            if string != "":
                ret.append(string)
        
        return ' '.join(ret[::-1])