class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)

        def Area(A,B,C):
            area = 0.5*abs((A[0]*(B[1]-C[1]))+(B[0]*(C[1]-A[1]))+(C[0]*(A[1]-B[1])))
            return round(area,5)

        maxArea = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    A,B,C = points[i], points[j], points[k]
                    area = Area(A,B,C)
                    if area>maxArea:
                        print(A,B,C,area,maxArea)
                        maxArea = area

        return maxArea