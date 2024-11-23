# Time Complexity: O(V + E)
# V: Number of vertices (nodes).
# E: Number of edges.

# Space Complexity: O(V)

from collections import deque

def bfs(root, target):
    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.value == target:
            return current
        queue.extend(current.children)
    return None
