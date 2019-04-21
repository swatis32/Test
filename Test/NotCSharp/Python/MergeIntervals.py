# https://www.youtube.com/watch?v=WdgAKCnWnwA
class Solution(object):
    stack = []

    def mergeIntervals(self, inputarr):
        Solution.stack = []
        inputarr.sort()
        self.push(inputarr[0])
        # print("Sorted array is" + str(inputarr))
        # print("Initial stack is " + str(Solution.stack))
        for i in range(len(inputarr)):
            if i==0:
                continue
            else:
                curr = inputarr[i]
                st = self.getTop()
                # if "start of curr" is in between current stack top limits AND "end of curr" is greater than end of stack top's end
                # it means, we can extend the interval by getting [start of stacktop, end of curr]
                if (curr[0] >= st[0] and curr[0] <= st[1]) and (curr[1] > st[1]):
                    # update end of stack top as end of curr
                    st[1] = curr[1]
                    # remove original stack top and add new modified stack top
                    self.pop()
                    self.push(st)
                    
                # if range of curr is completely within the stack top, then that element has already been merged into stack top so move on
                elif (curr[0] >= st[0] and curr[0] <= st[1]) and (curr[1] >= st[0] and curr[1] <= st[1]):
                    continue
                else:
                    self.push(curr)

        return Solution.stack

    def push(self, element):
        Solution.stack.append(element)

    def pop(self):
        Solution.stack = Solution.stack[:-1]


    def getTop(self):
        return Solution.stack[-1]

s = Solution()
print(s.mergeIntervals([[2,10],[7,12]]))
# should return [[2,12]]
print(s.mergeIntervals([[2,10],[7,12],[0,2]]))
# should return [[0,12]]
print(s.mergeIntervals([[2,10],[11, 12],[13, 18]]))
# should return the intervals as is as none of them overlap
print(s.mergeIntervals([[1, 5],[4, 7],[8, 19],[9, 29], [10, 14]]))
# should return [[1, 7], [8, 29]]
print(s.mergeIntervals([[1, 1000],[4, 7],[8, 19],[9, 29], [10, 14]]))
# should return [[1,1000]]
print(s.mergeIntervals([[1, 10],[4, 7],[8, 19],[4, 5], [100, 114]]))
# should return [[1, 19], [100, 114]]
