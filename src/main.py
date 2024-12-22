from src.user_input import *
from src.buildTree import *
from src.collection.tree import *
from src.evaluateTree import *

def main(print_tree = False):
    
    print("this is Yoav Mateless calculator \nWrite 'Exit' to quit")


    while (True):
        try:
            #GET INPUT
            input = Input()
            if input.getStr().strip().lower() == 'exit':
                break
            #BUILD TREE
            tree = TreeBuilder().build(input)
            #display tree
            if print_tree:
                tree.display()
            #EVALUATE TREE
            print(evaluateExpressionTree(tree))
        except Exception as exs:
            print(exs)



#function to calculate the expression
def calculate_expression(input_str):
    input_obj = Input(input_str)
    tree = TreeBuilder().build(input_obj)
    return evaluateExpressionTree(tree)




