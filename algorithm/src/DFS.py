def dfs(v):
    global rst
    if v == 'A':
        visited[v] = True
        rst += v + ' -> '
    for i in Graph[v]:
        if not visited[i]:
            visited[i] = True
            rst += i + ' -> '
            dfs(i)

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

    dfs('A')
    print(visited)
    print(rst)