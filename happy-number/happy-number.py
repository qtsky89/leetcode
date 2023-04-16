class Solution:
    def isHappy(self, n: int) -> bool:
        # n = 192

        visited = set()
        while n not in visited:
            visited.add(n)
            number_string = str(n)

            tmp = 0
            for s in number_string:
                tmp += int(s) ** 2

            if tmp == 1:
                return True
            n = tmp

        return False