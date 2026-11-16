class Solution:
    def rearrangeArray(self, nums):
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        ans = []

        while len(ans) < len(nums):
            for x in sorted(freq.keys()):
                if freq[x] > 0:
                    ans.append(x)
                    freq[x] -= 1

        return ans

# learn frequency mapping
# learn round robin loop