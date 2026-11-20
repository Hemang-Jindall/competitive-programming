class Solution:
    def minRotations(self, n: int, s: str) -> int:

        curr = 0
        total = 0

        for i in s:
            digit = int(i)
            diff = abs(curr - digit)
            total += min(diff, 10-diff)
            curr = digit
        ans = total
        last = int(s[-1])

        for k in range(n):
            prev = int(s[k-1]) if k > 0 else 0
            first = int(s[k])

            old_diff = abs(prev-first)
            old_cost = min(old_diff, 10-old_diff)

            new_diff = abs(prev-last)
            new_cost = min(new_diff, 10-new_diff)

            ans = min(ans, total-old_cost + new_cost)

        return ans


#trying to come up with the solution on my own accord
    