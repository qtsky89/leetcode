class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        s = ' a b c i i i d e f ' k = 3
              ^   ^
                ^   ^                  ret=1
                  ^   ^                ret=2
                    ^   ^              ret=3
        '''

        p1, p2 = 0, k-1

        current_vowel_count = 0
        for i in range(0, k):
            if s[i] in 'aeiou':
                current_vowel_count += 1

        max_vowel_count = 0
        while p2 <= len(s)-1:
            max_vowel_count = max(max_vowel_count, current_vowel_count)
            
            if p2+1 <= len(s)-1 and s[p2+1] in 'aeiou':
                current_vowel_count += 1
            
            if s[p1] in 'aeiou':
                current_vowel_count -= 1

            p1, p2 = p1+1, p2+1
        return max_vowel_count