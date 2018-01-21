from collections import defaultdict
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87736

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) is 0:
            return 0

        if k is 0:
            return len(s)

        dic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0,
               'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
               'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
               's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
               'y': 0, 'z': 0
               }

        for i in s:
            dic[i] += 1

        idx = 0
        while idx < len(s) and dic[s[idx]] >= k:
            idx += 1

        if idx == len(s):
            return len(s)

        left = self.longestSubstring(s[0:idx], k)
        right = self.longestSubstring(s[idx:], k)

        return max([left, right])
