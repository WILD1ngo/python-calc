from user_input import *
from buildTree import *
from collection.tree import *
from evaluateTree import *

def main():
    while (True):
        input = Input()
        tree = build(input)
        tree.display()
        print(evaluateExpressionTree(tree))




if __name__=="__main__":
    main()

