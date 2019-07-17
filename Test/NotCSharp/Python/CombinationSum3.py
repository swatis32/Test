# https://leetcode.com/problems/combination-sum-iii/submissions/
class Solution(object):
    def __init__(self):
        self.comb = []
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arr = set()
        self.helper(k, n, arr)
        return self.comb
    
    def helper(self, k, n, arr):
        if n < 0 or len(arr) > k:
            return
        
        if len(arr) == k and n == 0 and list(arr) not in self.comb:
            self.comb.append(list(arr))
            return
        
        for i in range(1,10):
            if i not in arr:
                arr.add(i)
                self.helper(k, n-i, arr)
                arr.discard(i)