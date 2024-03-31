class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)

        ret = sorted(s, key = lambda x: [c[x], x], reverse=True)

        return ''.join(ret)