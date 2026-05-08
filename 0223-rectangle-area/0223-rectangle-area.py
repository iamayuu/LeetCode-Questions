class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        #Area of a
        areaA = abs((ax2-ax1)*(ay2-ay1))

        #Area of b
        areaB = abs((bx2-bx1)*(by2-by1))

        #Combined area
        width = min(ax2,bx2)-max(ax1,bx1)
        height = min(ay2,by2)-max(by1,ay1)
        areaAB = abs(width*height) if width>0 and height>0 else 0
        return areaA+areaB-areaAB