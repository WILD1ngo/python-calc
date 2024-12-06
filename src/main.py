from user_input import *
from buildTree import *
from collection.tree import *


def main():
    #while(Settings.isRunning):
    input = Input()
    tree = build(input)
    tree.display()




if __name__=="__main__":
    main()

