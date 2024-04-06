class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret: list[list[int]] = []

        q = deque([set()])

        while q:
            item = q.popleft()

            ret.append(item)

            if len(item) == len(nums):
                break

            for n in nums:
                if not item or max(item) < n:
                    q.append(item | {n})

        return ret