class Solution(object):
    def minDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                total +=1
        return total
        