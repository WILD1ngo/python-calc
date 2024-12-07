from user_input import *
from buildTree import *
from collection.tree import *
from evaluateTree import *

def main():
    
    print("this is Yoav Mateless calcoulator \nWrite 'Exit' to quit")
    while (True):
        try:
            input = Input()
            if input.getStr() == 'Exit':
                break
            tree = build(input)
            #tree.display()
            print(evaluateExpressionTree(tree))
        except Exception as exs:
            if (len(exs.args) == 2):
                msg , location = exs.args
                print (msg)
                print(input.getStr())
                print(' ' * (location-1) + "^")
            else:
                print (exs)




if __name__=="__main__":
    main()

