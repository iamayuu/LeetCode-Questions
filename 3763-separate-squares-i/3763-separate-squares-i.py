class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        #Finding min_y, max_y and total area
        min_y = float("inf")
        max_y = float("-inf")
        totalArea = 0
        for x,y,l in squares:
            min_y = min(min_y, y)
            max_y = max(max_y, y+l)
            totalArea += (l*l)
        # print(f"min_y: {min_y}, max_y: {max_y}, totalArea: {totalArea}")
        
        low, high = min_y, max_y
        while high-low> 1e-5:
            mid_y = low+((high-low)/2)
            #Finding area below mid_y line
            bottomArea = 0
            for x,y,l in squares:
                if mid_y >= (y+l):
                    bottomArea += (l*l)
                elif mid_y > y:
                    bottomArea += (l*(mid_y-y))
            if bottomArea >= (totalArea/2):
                high = mid_y
            else:
                low = mid_y
        
        return low+((high-low)/2)
