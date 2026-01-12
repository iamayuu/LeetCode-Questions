class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        #in order to go from 1 point to another, the diagonal distance will be the minimum
        #of |x2-x1|, |y2-y1| and then we have to travel straignt for whichever distance is left
        #that means in total the steps will be eq to max(|x2-x1|,|y2-y1|)
        if len(points)==1:
            return 0
        
        ans = 0
        for i in range(1,len(points)):
            hori_dist = abs(points[i][0]-points[i-1][0])
            vert_dist = abs(points[i][1]-points[i-1][1])
            ans = ans + max(hori_dist, vert_dist)
        return ans