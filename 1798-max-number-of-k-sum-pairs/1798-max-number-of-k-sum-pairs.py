class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        c=0
        l=0
        r=len(nums)-1
        while l<r:
            sum=nums[l]+nums[r]
            if sum==k:
                l+=1
                r-=1
                c+=1
            elif sum<k:
                l+=1
            else:
                r-=1
        return c
