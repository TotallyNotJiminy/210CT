class BinTreeNode(object):

    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
  

def in_order(tree):
    if(tree.left!=None):
        in_order(tree.left)
    print(tree.value)
    if(tree.right!=None):
        in_order(tree.right)

def tree_sort(List):
    first=True
    for each in List:
        if first:
            t=tree_insert(None,each)
            first=False
        else:
            tree_insert(t,each)
    return t

if __name__ == '__main__':
    sortedlist=[6,10,5,2,3,4,11]
    t=tree_sort(sortedlist)
    in_order(t)s
