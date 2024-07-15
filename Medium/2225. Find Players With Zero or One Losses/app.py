class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        loser={}
        for w,l in matches:
            if w not in loser:
                loser[w]=0
            if l not in loser:
                loser[l]=0
            loser[l]+=1
        ans=[[], []]
        for k, v in loser.items():
            if v==0:
                ans[0].append(k)
            elif v==1:
                ans[1].append(k)
            

        return [sorted(ans[0]), sorted(ans[1])]


sol=Solution()
sol.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])