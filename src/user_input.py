from src.Istrable import *


class Input(Istrable):
         
        
    def __init__(self , raw_input = ""):
        if raw_input != "":
            self.raw_input = raw_input
        else :
            self.raw_input = input("> ")
        self.remove_spaces()
        
        
    def getStr(self):
        return self.raw_input

    def remove_spaces(self):
        self.raw_input = self.raw_input.replace(" ", "").replace("\t", "")