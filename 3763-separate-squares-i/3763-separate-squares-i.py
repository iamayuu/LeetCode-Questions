class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0        
        for x, y, l in squares:
            total_area += l * l
            
        events = []
        for x, y, l in squares:
            events.append((y, 1, l))
            events.append((y + l, 0, l))
        events.sort()
        opened = 0
        curr_area = 0
        prev_y = None
        for y, action, l in events:
            if prev_y != None:
                curr_area += opened * (y - prev_y)
            surplus = curr_area - total_area / 2
            if surplus == 0:
                return y
            if surplus > 0:
                return y - surplus / opened
            if action == 1:
                opened += l
            else:
                opened -= l
            prev_y = y
