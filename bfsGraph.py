from collections import deque

graph = {
    0:[1,2],
    1:[0,3,4],
    2:[0,4],
    3:[1],
    4:[1,2]
}

def bfs(root):
    visited = set()
    queue = deque()

    queue.append(root)
    visited.add(root)

    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal

print("bfs traversal: ", bfs(root))