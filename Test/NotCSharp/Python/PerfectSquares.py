import math
# https://leetcode.com/problems/perfect-squares/description/


class Solution(object):
    # https://discuss.leetcode.com/topic/26400/an-easy-understanding-dp-solution-in-java/20

    def numSquares(self, n):
        res = dict()
        res[0] = 0
        for i in range(1, n + 1):
            mini = 99999999
            j = 1
            while j * j <= i:
                mini = min(mini, res[i - j * j] + 1)
                j += 1
            res[i] = mini
        return res[n]

    # Wrong Method!!! Why? See example below
    def numSquares2(self, n):
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

        print("\n")
        print("Value of n is " + str(n))
        print("Value of c is " + str(c))
        print("a is " + str(a))
        print("b is " + str(b))
        return c

    def calcList(self, lower, upper, n, k):
        sumOfAllSq = 0
        list_nums = []
        if upper * upper == n or lower * lower == n:
            return [int(math.sqrt(n))]
        for x in range(k, 0, -1):
            while n - sumOfAllSq >= 0:
                sumOfAllSq = sumOfAllSq + x * x
                if n - sumOfAllSq >= 0:
                    list_nums.append(x)
            sumOfAllSq = sum(j*j for j in list_nums)

        return list_nums

    def sumOfSquares(self, i):
        return i/3 * (i + 1) * (i + 1/2)

    # Wrong solution!! Why? See 456 example below
    # This is NOT A knapsack problem which is bounded on "n"
    def numSquares3(self, n):
        result = []
        a = self.generateListSquares(n)
        for i in range(len(a) - 1, -1, -1):
            temp = a[i]
            if n < temp:
                continue
            else:
                while n >= temp:
                    n = n - temp
                    result.append(temp)
        return result

    def generateListSquares(self, n):
        i = 1
        result = []
        while i * i <= n:
            result.append(i * i)
            i += 1
        return result


s = Solution()
# Answer should be 1 (10 squared) but we get something else
s.numSquares2(100)

# print(s.numSquares(100))
# print(s.numSquares3(100))
# print(s.numSquares3(101))

print(s.numSquares(456))
print(s.numSquares3(456))

print(s.numSquares(95))
print(s.numSquares3(95))


