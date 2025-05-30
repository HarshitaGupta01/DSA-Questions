class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def rec(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                rec(i+1,path)
                path.pop()
        rec(0,[])
        return res
        