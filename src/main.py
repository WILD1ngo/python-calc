from src.user_input import *
from src.buildTree import *
from src.collection.tree import *
from src.evaluateTree import *

def main(print_tree = False):
    
    print("this is Yoav Mateless calculator \nWrite 'Exit' to quit")
    while (True):
        try:
            input = Input()
            if input.getStr().strip().lower() == 'exit':
                break
            tree = TreeBuilder().build(input)
            if print_tree:
                tree.display()
            print(evaluateExpressionTree(tree))
        except Exception as exs:
            print(exs)

def calculate_expression(input_str):
    input_obj = Input(input_str)
    tree = TreeBuilder().build(input_obj)
    return evaluateExpressionTree(tree)




if __name__=="__main__":
    main()

