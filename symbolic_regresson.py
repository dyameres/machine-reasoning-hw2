#
#
# By Dylan Ameres and Tristan Allen

from random import randrange

class Node():
    def __init__(self, value, left=None, right=None): #left and right are children
        self.left = left
        self.right = right
        self.value = value


class Tree():
    
    def createNode(self, data):
        """
        Utility function to create a node.
        """
        return Node(data)

    def insert(self, node, data):
        """
        Insert function will insert a node into tree.
        Duplicate keys are not allowed.
        """
        #if tree is empty , return a root node
        if node is None:
            return self.createNode(data)
        # if data is smaller than parent , insert it into left side
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node
        
    def getRoot(self):
        # return self.root
        return self
        
    def fitness(self,):
        # determine fitness of current tree
        # maybe mean square error
        return self
    
    def evaluate(self, x): # recursive
        return x
    
    def crossover(self, otherTree):
        # function for crossover
        return self
        
    def mutate(self,):
        # function for mutation
        return self


def buildTree(array):
    # array = [2, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2]
    tree1 = Node()
    rand_operator_num = randrange(1, 5)
    
    if rand_operator_num == 1:
        tree1.data = "+"
    elif rand_operator_num == 2:
        tree1.data = "-"
    elif rand_operator_num == 3:
        tree1.data = "*"
    elif rand_operator_num == 4:
        tree1.data = "/"


def main():
    rand_children = [2]
    for i in range(9):
        rand_children.append(randrange(0, 3, 2))
   
    print(rand_children)

if __name__ == "__main__":
    main()

# CITATIONS:
# https://www.researchgate.net/publication/10684490_Using_genetic_programming_to_discover_nonlinear_variable_interactions