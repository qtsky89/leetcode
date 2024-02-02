class Solution:
    def __init__(self):
        self._vowels = "aeiouAEIOU"

    def reverseVowels(self, s: str) -> str:
        '''
        reverse only a e i o u

        l e e t c o d e
          ^           ^

        case1. if pointer represent not vowel then, skip it
        case2. if it are both vowel than switch with the other pointer
        until the pointer met each other
        '''

        ret = list(s)
        l, r = 0, len(ret)-1
        
        while l < r:
            # switch it!
            if ret[l] in self._vowels and ret[r] in self._vowels:
                ret[l], ret[r] = ret[r], ret[l]
                l += 1
                r -= 1
            elif ret[l] not in self._vowels:
                l += 1
            elif ret[r] not in self._vowels:
                r -= 1
            else:
                l += 1
                r -= 1
        return ''.join(ret)

            


        