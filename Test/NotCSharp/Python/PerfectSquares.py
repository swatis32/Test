import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 0
        upper = 0
        for i in range(0, n+1):
            ss = self.sumOfSquares(i)
            if ss <= n:
                lower = i
                continue
            if ss > n:
                upper = i
                break

        a = self.calcList(lower, upper, n, lower)
        b = self.calcList(lower, upper, n, upper)

        c = min(len(a), len(b))
        if c == 0 and len(a) == 1:
            return len(a)

        if c == 0 and len(b) == 1:
            return len(b)

        print(c)
        return c

    def calcList(self, lower, upper, n, k):
        sumOfAllSq = 0
        list_nums = []
        if upper * upper == n or lower * lower == n:
            return [math.sqrt(n)]
        for x in range(k, 0, -1):
            while n - sumOfAllSq >= 0:
                sumOfAllSq = sumOfAllSq + x * x
                if n - sumOfAllSq >= 0:
                    list_nums.append(x)
            sumOfAllSq = sum(j*j for j in list_nums)

        return list_nums

    def sumOfSquares(self, i):
        return i/3 * (i + 1) * (i + 1/2)


s = Solution()
s.numSquares(14)