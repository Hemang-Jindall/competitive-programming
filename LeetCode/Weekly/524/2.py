class Solution(object):
    def lastVisitedCell(self, grid):
        x = 0
        y = 0

        seen = {(0, 0)}

        while True:
            direction = grid[x][y]

            if direction == "R":
                ny, nx = y + 1, x
            elif direction == "L":
                ny, nx = y - 1, x
            elif direction == "D":
                nx, ny = x + 1, y
            elif direction == "U":
                nx, ny = x - 1, y

            if not (0 <= nx < len(grid) and
                    0 <= ny < len(grid[0])):
                return [x, y]

            if (nx, ny) in seen:
                return [x, y]

            x, y = nx, ny
            seen.add((x, y))