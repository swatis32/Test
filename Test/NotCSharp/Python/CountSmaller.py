# https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
# Correct solution - this is O(n2) though - takes too long, look at java code for the same file name - CountSmaller.


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        dic = dict()
        dic[len(nums) - 1] = 0

        for i in range(len(nums) - 2, -1, -1):
            temp = nums[i:]
            ele = nums[i] * -1
            temp[:] = [x + ele for x in temp]
            count = len([y for y in temp if y < 0])
            dic[i] = count

        result = []
        for k, v in dic.items():
            result.append(v)

        return result