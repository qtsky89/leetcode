class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        for num in arr:
            dp[num] = 1
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    j = num // i
                    if i in dp and j in dp:
                        dp[num] += dp[i] * dp[j] * (1 if i == j else 2)
            dp[num] %= MOD
        return sum(dp.values()) % MOD