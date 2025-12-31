"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = []
        end_times = []
        for i in range(len(intervals)):
            start_times.append(intervals[i].start)
            end_times.append(intervals[i].end)
        start_times.sort()
        end_times.sort()

        count = 0
        max_count = 0
        i=0
        j=0
        while j<len(end_times):
            if i< len(start_times) and min(start_times[i],end_times[j])!=end_times[j]:
                count+=1
                max_count = max(max_count, count)
                i+=1
            else:
                count -=1
                j+=1
        return max_count





