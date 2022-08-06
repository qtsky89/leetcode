# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n: int):
        if n == 1:
            return 1
        
        """
        :type n: int
        :rtype: int
        """
        p1, p2 = 1, n
        
        # 1(good),2(good),3(good),4(bad),5(bad)
        #iter1 p1 = 1, p2 = 5 mid = 3
        #iter2 p1 = 4, p2 = 5 mid = 4
        while p1 <= p2:
            mid = (p1 + p2) // 2

            if self.is_first_bad_version(mid):
                return mid
            elif isBadVersion(mid):
                p2 = mid
            else:
                p1 = mid + 1
        
    def is_first_bad_version(self, target: int) -> bool:
        if isBadVersion(target) and (target == 1 or not isBadVersion(target-1)):
            return True
        else:
            return False