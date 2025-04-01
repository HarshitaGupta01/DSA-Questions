class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def recur(s,open,close):
            if len(s)==2*n:
                res.append(s)
            if open<n:
                recur(s+"(",open+1,close)
            if close<open:
                recur(s+")",open,close+1)
        recur("",0,0)
        return res

        