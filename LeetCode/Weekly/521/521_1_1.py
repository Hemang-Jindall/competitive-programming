class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        # learn how to do indexing for an interval based array
        ans = 0
        intervals.sort()
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if intervals[i][1] >= intervals[j][0]:
                    ans +=1
        return ans
    
#struggled slightly with the loop boundaries