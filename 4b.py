def bfs(root=None):
    if root is None:
        return
    queue = [root]
    while len(queue) > 0:
        cur_node = queue.pop(0)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)


def bfs(self, root=None):
    if root is None:
        return

    queue = [root]
    while len(queue) > 0:
        cur_node = queue.pop(0)
        if cur_node.left is not None:
            queue.append(cur_node.left)
        if cur_node.right is not None:
            queue.append(cur_node.right)

# start BFS traversal after initializing the tree
root = Node(4)
root.inse