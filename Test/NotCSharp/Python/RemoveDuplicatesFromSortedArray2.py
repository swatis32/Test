 #https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in range(0, len(nums)):
            if i == 0:
                result.append(nums[i])
                continue
            if nums[i] in result and result.count(nums[i]) == 1:
                result.append(nums[i])
                continue

            if nums[i] not in result:
                result.append(nums[i])

        [print(k) for k in result]
        return len(result)

s = Solution()
s.removeDuplicates([1,1,1,2])
