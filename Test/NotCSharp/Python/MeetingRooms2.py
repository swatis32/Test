# https://www.youtube.com/watch?v=GmpyAMpjpUY
# the above has an excellent explanation to use minheap
# we will try the approach used in MeetingRooms.py, followed by above heap solution

# my approach is below - wont work for an example like [[1,2],[2,3]]. 
# This will say 2 meeting rooms are needed, whereas we need 1
import sys
def getNumMeetingRooms(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    
    maxtime = 0
    mintime = sys.maxsize
    for meet in arr:
        maxtime = max(maxtime, meet[1])
        mintime = min(mintime, meet[0])

    maxcount = 0
    for i in range(mintime, maxtime+1):
        count = 0
        for meet in arr:
            if meet[0] <= i <= meet[1]:
                count +=1
        if count > maxcount:
            maxcount = count
    return maxcount

print(getNumMeetingRooms([[1,2],[2,3]]))

