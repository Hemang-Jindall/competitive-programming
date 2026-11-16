# Problem: A. In the Dream
# One sentence: Check if goals in each half could happen without 3-in-a-row for either team.
# Category: Math/constructive.
# Constraints: t large, values big -> need O(1) formula.
# First instinct: Find max allowed ratio between two teams' goals in a half.
# Other approach: max(x,y) <= 2*min(x,y)+2 per half.
# Gotcha: second half scores are (c-a, d-b), not (c,d).


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        current = ""
        largest = ""

        def pali(item):
            if list(item) == list(reversed(item)):
                return True
            else:
                return False

        for i in range(len(s)):
            current +=s[i]
            if pali(current):
                continue
            else:
                current.remove[0]
            if len(current) > len(largest):
                largest = current

        return largest
