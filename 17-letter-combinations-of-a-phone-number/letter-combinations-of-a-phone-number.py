class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dic = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        ret = []

        def dfs(current: str) -> None:
            if len(current) == len(digits):
                ret.append(current)
                return

            i = len(current)

            key = digits[i]
            for value in dic[key]:
                dfs(current + value)

        dfs('')

        return ret