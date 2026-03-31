class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        
        n=len(nums3)-1
        mid=n//2
        if n%2==0:
            return nums3[mid]
        else:
            return (nums3[mid]+nums3[mid+1])/2