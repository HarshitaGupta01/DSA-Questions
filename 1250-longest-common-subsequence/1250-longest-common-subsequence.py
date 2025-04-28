class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # # ==recursion=====================
        # def rec(i,j):
        #     if i==len(text1) or j==len(text2):
        #         return 0
        #     if text1[i]==text2[j]:
        #         return 1+rec(i+1,j+1)
        #     else:
        #         return max(rec(i+1,j), rec(i,j+1))
        # return rec(0,0)

        # ========memoization===========
        memo={}
        def rec(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i]==text2[j]:
                return 1+rec(i+1,j+1)
            else:
                memo[(i,j)]= max(rec(i+1,j), rec(i,j+1))
                return memo[(i,j)]
        return rec(0,0)


        