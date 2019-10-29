def bfs(v):
    global rst
    visited[v] = True
    queue = [v]
    while queue:
        now = queue.pop(0)
        rst += now + ' -> '
        for i in Graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

if __name__ == "__main__":
    Graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D', 'G'],
        'D': ['C', 'E'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }
    visited = dict(zip([v for v in Graph], [False for _ in Graph]))
    rst = ''

    bfs('A')
    print(visited)
    print(rst)