# Time Complexity: O(V + E)
# V: Number of vertices (nodes).
# E: Number of edges.

# Space Complexity: O(h)
# h: Height of the tree.

def dfs(root, target, path=()):
    path = path + (root,)
    if root.value == target:
        return path
    for child in root.children:
        path_found = dfs(child, target, path)
        if path_found is not None:
            return path_found
    return None
