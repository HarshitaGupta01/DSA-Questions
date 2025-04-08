class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # ====recursion=========
        # if n<=1:
        #     return n
        # else:
        #     return self.fib(n-1)+ self.fib(n-2)

        # =========
        dp=[0]*(n+1)
        if n<=1:
            return n
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]