class Node(object):

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class TreeNode(object):
    """docstring for TreeNode."""

    def __init__(self):
        self.root = None
        self.count = 0
        self.height = 0

    def isLeaf(self, node):
        return node.left is None and node.right is None

    def addNode(self, data):
        if self.root is None:
            self.root = Node(data, None, None)
        else:
            node = self.root
            while not self.isLeaf(node):
                if node.data > data:
                    if node.left is not None:
                        node = node.left
                    else: break
                else:
                    if node.right is not None:
                        node = node.right
                    else: break
            if node.data > data:
                node.left = Node(data, None, None)
            else:
                node.right = Node(data, None, None)
            if self.isLeaf(node):
                self.heightTree()
        self.count += 1

    def searchNode(self, data):
        node = self.root
        while node is not None:
            if node.data == data:
                break
            if node.data > data:
                node = node.left
            else:
                node = node.right
        if node is None:
            return
        return node

    def search(self, data):
        if self.searchNode(data) is None:
            return "Node not in Tree"
        return 'Node in Tree'

    def heightGivenTree(self, node):
        if node is None:
            return 0
        else:
            l_height = self.heightGivenTree(node.left)
            r_height = self.heightGivenTree(node.right)

            if l_height > r_height:
                return (l_height + 1)
            else:
                return (r_height + 1)

    def heightTree(self):
        if self.root is not None:
            self.height = self.heightGivenTree(self.root)
        return self.height

    def displayGivenTree(self, node, level):
        if node is None:
            return
        else:
            self.displayGivenTree(node.left, level+1)
            self.displayGivenTree(node.right, level+1)

            self.display[level].append(node.data)

    def __str__(self):
        self.display = [[] for i in range(self.heightTree())]
        self.displayGivenTree(self.root, 0)
        l = []
        for i in self.display:
            l.extend(i)
        return str(l)

def main():
    myTree = TreeNode()
    myTree.addNode(10)
    myTree.addNode(5)
    myTree.addNode(15)
    myTree.addNode(3)
    myTree.addNode(7)
    myTree.addNode(13)
    myTree.addNode(17)
    myTree.addNode(1)
    myTree.addNode(2)
    myTree.addNode(4)
    myTree.addNode(6)
    myTree.addNode(9)
    myTree.addNode(12)
    myTree.addNode(11)
    myTree.addNode(14)
    myTree.addNode(8)
    myTree.addNode(16)
    myTree.addNode(18)

    print(myTree.heightTree())
    print(myTree)
    print(myTree.search(2))
    print(myTree.search(200))

if __name__ == '__main__':
    main()
