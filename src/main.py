from user_input import *
from buildTree import *
from collection.tree import *
from evaluateTree import *

def main():
    
    print("this is Yoav Mateless calculator \nWrite 'Exit' to quit")
    while (True):
        try:
            input = Input()
            if input.getStr().strip().lower() == 'exit':
                break
            tree = TreeBuilder().build(input)
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

