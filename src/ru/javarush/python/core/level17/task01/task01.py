# Бинарное дерево

# Напишите функцию для вставки нового элемента в бинарное дерево поиска (BST).
# Функция должна принимать корневой узел дерева и значение нового элемента и возвращать обновленное дерево.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# class TreeNode:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key


def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.value:
        root.left = insert(root.left, key)
    elif key > root.value:
        root.right = insert(root.right, key)
    return root