class Solution:
    def delete_count(self,base_string: str, word: str) -> int:
        p1, p2 = 0, 0

        while p1 <= len(base_string)-1 and p2 <= len(word)-1:
            if base_string[p1] == word[p2]:
                p1 += 1
                p2 += 1
            else:
                p1 += 1
        
        if p2 == len(word):
            return len(base_string) - len(word)
        else:
            return float('inf')

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ret = ''
        min_count = float('inf')
        dictionary.sort()
        for word in dictionary:
            tmp = self.delete_count(s, word)
            if tmp < min_count:
                ret = word
                min_count = tmp
        return ret

            