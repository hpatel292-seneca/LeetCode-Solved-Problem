class UnionFind:
        def __init__(self):
            self.parent={}
            self.rank={}

            for c in 'abcdefghijklmnopqrstuvwxyz':
                self.parent[c]=c
                self.rank[c]=0
        
        def find(self, x):
            if self.parent[x]!=x:
                self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            rootx=self.find(x)
            rooty=self.find(y)

            if rootx!=rooty:
                if self.rank[rootx]>self.rank[rooty]:
                    self.parent[rooty]=rootx
                elif self.rank[rootx]<self.rank[rooty]:
                    self.parent[rootx]=rooty
                else:
                    self.parent[rootx]=rooty
                    self.rank[rooty]+=1

class Solution(object):

    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        uf=UnionFind()

        for eq in equations:
            if eq[1]=='=':
                uf.union(eq[0], eq[3])
        
        for eq in equations:
            if eq[1]=='!':
                rootx=uf.find(eq[0])
                rooty=uf.find(eq[3])
                if rootx==rooty:
                    return False
        
        return True
