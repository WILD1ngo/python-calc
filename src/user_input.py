from Istrable import *


class Input(Istrable):
         
        
    def __init__(self):
        self.raw_input = input("> ")
        
    def getStr(self):
        return self.raw_input