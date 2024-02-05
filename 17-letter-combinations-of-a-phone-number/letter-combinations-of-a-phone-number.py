class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        digits = "23"

        step1. make hash map
        {
            2 : [a,b,c]
            3
            4
            5
            6
            7
            8
            9
        }
        '''
        if digits == "":
            return []

        digit_letter_map = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z'],
        }

        q = deque([""])

        ret = []
        while q:
            item = q.popleft()

            if len(item) == len(digits):
                ret.append(item)
                continue
            
            # len(item) => 0

            # char => a, b, c...
            i = len(item)
            for char in digit_letter_map[digits[i]]:
                q.append(item + char)
        return ret
        
            