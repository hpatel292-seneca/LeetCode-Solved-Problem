def bfs(graph, start, res=set()):
    visited=[]
    visited.append(start)

    while visited:
        start=visited[0]
        visited.pop(0)
        res.add(start)

        for i in graph[start]:
            if i not in res:
                visited.append(i)

visited=set()
res=set()
bfs([[2,1],[3],[3],[]], 0, res)
print(res)



