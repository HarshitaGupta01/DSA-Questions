class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxres=nums[0]
        maxpos=nums[0]
        minneg=nums[0]
        ch1=0
        ch2=0
        for i in range(1,len(nums)):
            ch1=maxpos*nums[i]
            ch2=minneg*nums[i]
            maxpos=max(nums[i],ch1,ch2)
            minneg=min(nums[i],ch1,ch2)
            maxres=max(maxres, maxpos, minneg)
        return maxres
        