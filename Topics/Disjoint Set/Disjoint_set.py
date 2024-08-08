class UnionFind:
    def __init__(self):
        self.parent={}
        self.rank={}
    
        for c in 'abcdefghijklmnopqrstuvwxyz':
            self.parent[c] = c
            self.rank[c] = 0
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # Path compression for efficiency
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootX] = rootY
                self.rank[rootY]+=1
    
    