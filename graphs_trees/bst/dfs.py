def in_order_traversal(node, visit_func):
    if node is not None:
        in_order_traversal(node.left, visit_func)
        visit_func(node.data)
        in_order_traversal(node.right, visit_func)

def pre_order_traversal(node, visit_func):
    if node is not None:
        visit_func(node.data)
        pre_order_traversal(node.left, visit_func)
        pre_order_traversal(node.right, visit_func)

def post_order_traversal(node, visit_func):
    if node is not None:
        post_order_traversal(node.left, visit_func)
        post_order_traversal(node.right, visit_func)
        visit_func(node.data)