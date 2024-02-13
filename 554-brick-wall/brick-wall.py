class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = {0:0}

        for r in wall:
            total = 0
            for v in r[:-1]:
                total += v
                count[total] = 1 + count.get(total,0)
        return len(wall) - max(count.values())