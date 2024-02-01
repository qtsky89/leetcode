class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = []

        i, j = 0, 0
        while i <= len(word1)-1 and j <= len(word2)-1:
            ret.append(word1[i])
            ret.append(word2[j])

            i, j = i+1, j+1
        
        while i <= len(word1)-1:
            ret.append(word1[i])
            i+=1
        
        while j <= len(word2)-1:
            ret.append(word2[j])
            j+=1
        
        return ''.join(ret)

        