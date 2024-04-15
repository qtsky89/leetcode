class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)

        x = sorted(s, key=lambda x: [c[x], x], reverse=True)

        return ''.join(x)

