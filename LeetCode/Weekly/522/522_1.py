class Solution:
    def minRotations(self, s: str) -> int:
        curr = 0
        total = 0
        for i in s:
            if i == curr:
                continue
            else:
                total += min(abs(curr-int(i))), 10-(abs(curr-int(i)))
            curr = i
        return total

#solution without AI