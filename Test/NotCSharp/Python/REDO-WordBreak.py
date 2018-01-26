# https://leetcode.com/problems/word-break/description/
class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True # empty string is always true
        for i in range(len(s)):
            print("dp[i]", i, dp[i])
            for j in range(i, len(s)):
                print("s[i: j + 1]", i, j, s[i: j + 1])
                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j + 1] = True
                    print("dp[j + 1] was made True", j+1)
        print(dp)
        return dp[-1]

s = Solution()
# s.wordBreak("cars", ["car", "ca", "rs"])
s.wordBreak("goalspecial", ["go","goal","goals","special"])


# much easier to understand, however, this is not optimal as this re-calculates the same result several times
class Solution2(object):
    def wordBreak(self, s, wordDict):
        if len(s) is 0:
            return True

        i = 1
        while i <= len(s):
            if s[:i] in wordDict:
                res = self.wordBreak(s[i:], wordDict)
                if res:
                    return res
            i += 1
        return False