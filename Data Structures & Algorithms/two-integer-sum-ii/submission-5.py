class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
        if not nums:
            return
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i+1, j+1]