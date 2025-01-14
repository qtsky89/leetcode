class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ret = []

        for word in words:
            tmp = word.split(separator)

            for t in tmp:
                if t != '':
                    ret.append(t)
        return ret