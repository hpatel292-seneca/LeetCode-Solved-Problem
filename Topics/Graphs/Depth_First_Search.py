# Recursive solution we are not using any Stack for storing elements as we are making recursive calls.
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

visited=set()
dfs([[2,1],[3],[3],[]], 0, visited)
# print(visited)


# Iterative way for DFS.
def dfs_iterative(graph):
    stack=[]
    visited=set()
    stack.append(0)
    arr=[]
    min_height=0
    while stack:
        curr=stack.pop()
        visited.add(curr)
        arr.append(curr)
        for i in graph[curr]:
            if i not in visited:
                stack.append(i)
        
    return arr

print(dfs_iterative([[2,1],[3],[3],[]]))
