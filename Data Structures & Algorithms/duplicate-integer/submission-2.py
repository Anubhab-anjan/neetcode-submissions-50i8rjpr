class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            n=set(nums)
            if len(nums) != len(n):
                return True
            
        return False