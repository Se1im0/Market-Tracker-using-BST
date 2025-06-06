from TreeNode import TreeNode

def inorder(node):
    res = []
    if node is None:
        return []
    
    res.extend(inorder(node.left))
    res.append(node.key)
    res.extend(inorder(node.right))

    return res

def preorder(node):
    res = []
    if node is None:
        return []
    
    res.append(node.key)
    res.extend(preorder(node.left))
    res.extend(preorder(node.right))
    
    return res

def postorder(node):
    res = []
    if node is None:
        return []
    
    res.extend(postorder(node.left))
    res.extend(postorder(node.right))
    res.append(node.key)
    
    return res
