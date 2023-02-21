#
#
# By Dylan Ameres and Tristan Allen

from random import randrange

class Node():
    def __init__(self, parent, value, left=None, right=None): #left and right are children
        self.left = left
        self.right = right
        self.value = value
    
    def insert(self, value):
      if self.value:
         if value < self.value:
            if self.left is None:
               self.left = Node(value)
            else:
               self.left.insert(value)
         elif value > self.value:
            if self.right is None:
               self.right = Node(value)
            else:
               self.right.insert(value)
         else:
            self.value = value


class Tree():
    def __init__(self, root):
        # comment
        # define self.root = root
        # if statements for operators 
        # else must be integers 
        self.root = root
        
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


def main():
    rand_children = []
    for i in range(10):
        rand_children.append(randrange(0, 3, 2))
   
    print(rand_children)

if __name__ == "__main__":
    main()

# CITATIONS:
# https://www.researchgate.net/publication/10684490_Using_genetic_programming_to_discover_nonlinear_variable_interactions