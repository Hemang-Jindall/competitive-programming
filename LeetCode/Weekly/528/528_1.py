class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        #find smallest element
        #calculate bitwise and of all the elements encountered thus far
        n = len(nums)
        count = 0
        for i in range(n):
            mn = nums[i]
            and_val = nums[i]
            for j in range(i,n):
                mn = min(mn, nums[j])
                and_val &= nums[j]

                if mn == and_val:
                    count+=1
        return count