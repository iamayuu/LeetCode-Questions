class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        robots = [[a,b,c,d] for a,b,c,d in zip(range(len(positions)), positions, healths, directions)] # index, position, health, direction
        robots.sort(key=lambda x:x[1]) # sort by starting position
        for robot in robots:
            destroyed = False
            while not destroyed and stack and stack[-1][-1] == "R" and robot[-1] == "L":
                prev = stack.pop()
                if prev[2] < robot[2]:
                    robot[2] -= 1
                elif prev[2] == robot[2]:
                    destroyed = True
                else:
                    destroyed = True
                    prev[2] -= 1
                    stack.append(prev)
            if not destroyed:
                stack.append(robot)
        stack.sort(key=lambda x:x[0]) # sort by index to return to original ordering
        return [x[2] for x in stack]