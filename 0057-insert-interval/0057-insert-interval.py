class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Solution1 (Brute Force)
        # if len(intervals)==0:
        #     intervals.append(newInterval)
        # elif intervals[0][0]>newInterval[0]:
        #     intervals.insert(start, newInterval)
        # elif intervals[-1][0]<newInterval[0]:
        #     intervals.append(newInterval)
        # else :
        #     start = 0
        #     end = len(intervals)-1
        #     while start<=end:
        #         mid = (start+end)//2
        #         if start==mid:
        #             if intervals[start][0]<=newInterval[0]:
        #                 intervals.insert(start+1, newInterval)
        #             else:
        #                 intervals.insert(start, newInterval)
        #             break
        #         elif end==mid:
        #             intervals.insert(end, newInterval)
        #             break
        #         elif intervals[start][0]<=newInterval[0]<=intervals[mid][0]:
        #             end=mid
        #         else:
        #             start=mid
        # result = []
        # result.append(intervals[0])
        # for i in range(1, len(intervals)):
        #     if result[-1][1]>=intervals[i][0]:
        #         result[-1][1]=max(intervals[i][1],result[-1][1])
        #     else:
        #         result.append(intervals[i])
        # return result
    
        #Solution2 (Using Greedy Algorithm)
        result = []
        i = 0
        n = len(intervals)
        merge_low = newInterval[0]
        merge_high = newInterval[1]
        while i<n and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=newInterval[1]:
            merge_low = min(intervals[i][0], merge_low)
            merge_high = max(intervals[i][1], merge_high)
            i+=1
        result.append([merge_low, merge_high])
        while i<n:
            result.append(intervals[i])
            i+=1
        return result
