# brute force: 1(a), 2(b), 3(c), b >= (a+c)/2

class Solution:
    def countDominantElements(self, nums: list[int]) -> int:

        count = 0

        for i in range(len(nums)):
            if len(nums) == 1:
                count+=1
                break
            if i == 0:
                if nums[i] >= nums[i+1]:
                    count+=1
            elif i == len(nums)-1:
                if nums[i] >= nums[i-1]:
                    count+=1
                    break
            else:
                if nums[i] >= (nums[i+1] + nums[i-1])/2:
                    count+=1
        return count

#accepted without any help, simple debugging