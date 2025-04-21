class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxsum=arr[0]
        mw=0
        mwo=arr[0]
        n=len(arr)
        for i in range(1,n):
            mw=max(mwo,mw+arr[i])
            mwo=max(mwo+arr[i],arr[i])
            maxsum=max(maxsum,mw,mwo)
        return maxsum
        