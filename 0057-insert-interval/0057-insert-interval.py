class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start = 0
        end = len(intervals)-1
        if len(intervals)==0:
            intervals.append(newInterval)
        elif intervals[0][0]>newInterval[0]:
            intervals.insert(start, newInterval)
        elif intervals[-1][0]<newInterval[0]:
            intervals.append(newInterval)
        else :
            while start<=end:
                mid = (start+end)//2
                if start==mid:
                    if intervals[start][0]<=newInterval[0]:
                        intervals.insert(start+1, newInterval)
                    else:
                        intervals.insert(start, newInterval)
                    break
                elif end==mid:
                    intervals.insert(end, newInterval)
                    break
                elif intervals[start][0]<=newInterval[0]<=intervals[mid][0]:
                    end=mid
                else:
                    start=mid
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[-1][1]>=intervals[i][0]:
                result[-1][1]=max(intervals[i][1],result[-1][1])
            else:
                result.append(intervals[i])
        return result
