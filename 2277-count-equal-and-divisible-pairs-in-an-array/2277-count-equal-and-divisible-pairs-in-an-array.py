class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        c=0
        for i in range(n):
            for j in range(i+1,n):
                if (i*j)%k==0 and nums[i]==nums[j]:
                    c+=1
        return c