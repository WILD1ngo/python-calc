from UI.main_UI import App
from src.main import *


#Settings:
UI = True #If True, the program will run the UI, else it will run the console version
PrintTree = False # If True, the program will print the tree before calculating the expression 




if __name__ == "__main__":


    if UI:
        app = App()
        app.mainloop()
    else:
        main(PrintTree)

