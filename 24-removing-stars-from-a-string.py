class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in s :
            if (i) == "*" and len(res) > 0:
                res.pop()
            else:
                res.append(i)
        return (''.join(res))