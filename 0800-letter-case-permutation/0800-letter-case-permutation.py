class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        def rec(i,path):
            if i==len(s):
                res.append("".join(path))
                return
            if s[i].isalpha():
                path.append(s[i].lower())
                rec(i+1,path)
                path.pop()

                path.append(s[i].upper())
                rec(i+1,path)
                path.pop()
            else:
                path.append(s[i])
                rec(i+1,path)
                path.pop()
        rec(0,[])
        return res
        
        