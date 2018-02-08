#https://leetcode.com/problems/largest-number/description/
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber2(self, nums):
        result = ""
        desc_list = [9,8,7,6,5,4,3,2,1]
        for i in desc_list:
            candidates = [j for j in nums if int(str(j)[0:1]) == i]
            if len(candidates) is 0:
                continue
            else:
                if len(candidates) == 1:
                    num = max(candidates)
                if len(candidates) > 1:
                    # This is a wrong solution as simple sorting wont work, example [121,12] => 12121, not 12112
                    candidates = sorted(candidates, reverse=True)
                    num = ''.join(str(k) for k in candidates)
                result = result + str(num)

        return result

    # not optimal, dont use!!
    def largestNumber(self, nums):
        maximum = ''
        import itertools
        for x in itertools.permutations(nums, len(nums)):
            tmp = ''.join(str(k) for k in x)
            if tmp > maximum:
                maximum = tmp

        print(maximum)
        if maximum[:1] is '0' and maximum[len(maximum) - 1:len(maximum)] is '0':
            return 0
        else:
            return maximum

s = Solution()
s.largestNumber(nums=[1,2,3,4,5,6,7,8,9,0])