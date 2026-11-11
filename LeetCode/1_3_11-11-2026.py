class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        dict = {}
        nums.sort()

        for i in nums:
            dict[i] = dict.get(i,0) + 1
            # need to learn the get function, dict basics

        ans = []

        while len(ans) < len(nums):
            for i in sorted(dict.keys()):
                if dict[i] > 0:
                    ans.append(i)
                    dict[i] -=1
                    # curious about how a single instance of each element gets added during the cycle
        return ans