# Problem: A. In the Dream
# One sentence: Check if goals in each half could happen without 3-in-a-row for either team.
# Category: Math/constructive.
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Find max allowed ratio between two teams' goals in a half.
# Other approach: max(x,y) <= 2*min(x,y)+2 per half.
# Gotcha: second half scores are (c-a, d-b), not (c,d).


class Solution(object):
    def reverse(self, x):
        x_str = str(x)

        x_list = list(str(x))

        x_rev_list = reversed(list(str(x)))

        x_int = int(x_rev_list)

        return x_int

