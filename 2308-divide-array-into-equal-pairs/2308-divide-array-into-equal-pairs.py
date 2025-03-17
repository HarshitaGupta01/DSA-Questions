class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in d.values():
            if j%2!=0:
                return False
        return True
        