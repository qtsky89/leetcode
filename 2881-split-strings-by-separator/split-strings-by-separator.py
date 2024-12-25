class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        '''
        Input: words = ["one.two.three","four.five","six"], separator = "."

        Output: ["one","two","three","four","five","six"]
        '''

        ret = []

        for word in words:
            tmp = word.split(separator)

            tmp_filter = []
            for t in tmp:
                if t != "":
                    tmp_filter.append(t)

            ret += tmp_filter
        return ret