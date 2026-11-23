class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')

        for i in range(0, len(nums), 2):
            merged = int(str(nums[i]) + str(nums[i + 1]))
            ans = min(ans, merged)

        return ans