class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # res=[]
        intervals.sort()
        i=0
        for j in range(1,len(intervals)):
            if intervals[i][1]>=intervals[j][0]:
                # res.append((intervals[i][0],intervals[i+1][1]))
                intervals[i][1]=max(intervals[i][1],intervals[j][1])

            else:
                i+=1
                intervals[i]=intervals[j]
                # res.append(intervals[i])
        # return res
        return intervals[:i+1]