class Solution(object):
    def climbStairs(self, n,memo=None):
        """
        :type n: int
        :rtype: int
        """
        # ============Tabulation==================
        # if n<=2:
        #     return n
        # dp=[0]*(n+1) #creates list of size (n+1)so that we can access dp[n]as indexing starts with 0
        # dp[1]=1
        # dp[2]=2
        # for i in range(3,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[i]

    # ===================Memoization=========================
        if memo is None:
            memo={}
        if n<=2:
            return n
        if n in memo:
            return memo[n]
        memo[n]=self.climbStairs(n-1,memo)+self.climbStairs(n-2,memo)
        return memo[n]

        