class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # ==recursion===================dfs=============
        # def rec(idx):
        #     if idx==len(s):
        #         return True
        #     for i in range(idx+1,len(s)+1):
        #         if s[idx:i] in wordDict and rec(i):
        #             return True
        #     return False
        # return rec(0)

        # =======memoization==========
        memo={}
        def rec(idx):
            if idx==len(s):
                return True
            if idx in memo:
                return memo[idx]
            for i in range(idx+1,len(s)+1):
                if s[idx:i] in wordDict and rec(i):
                    memo[idx]=True
                    return True
            memo[idx]=False
            return False
        return rec(0)



        