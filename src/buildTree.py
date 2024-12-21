from src.Istrable import *
from src.collection.tree import *
from src.Exeptions import *


class TreeBuilder:
    def __init__(self):
        self.p = [0] * 127
        self.p[ord('+')] = self.p[ord('-')] = 1
        self.p[ord('/')] = self.p[ord('*')] = 2
        self.p[ord('^')] = 3
        self.p[ord('%')] = 4
        self.p[ord('$')] = self.p[ord('@')] = self.p[ord('&')] = 5
        self.p[ord('~')] = self.p[ord('!')] = self.p[ord('#')] = 6
        self.p[ord(')')] = 0
    def handle_digits(self,s: str, i: int, two_digits_in_row: bool, stN: list, stC: list) :
        if two_digits_in_row:
            stC.append('+')
        num = ""
        if s[i] == '-' and s[i+1].isdigit():
            num += s[i]
            i+=1
        while i < len(s) and (s[i].isdigit() or s[i] == '.' or s[i] == ' '):
            if s[i] == ' ':
                i += 1
                continue
            num += s[i]
            i += 1
        i -= 1
        t = newNode(float(num))
        stN.append(t)
        return i, True

    def handle_operator(self, s: str, i: int, stN: list, stC: list):
        self.validate_operator(s, i)
        while len(stC) != 0 and stC[-1] != '(' and \
                ((s[i] != '^' and self.p[ord(stC[-1])] >= self.p[ord(s[i])]) or
                (s[i] == '^' and self.p[ord(stC[-1])] > self.p[ord(s[i])])):
            self.process_operator(stN, stC)

        
        if s[i] == '~' and (s[i-1].isdigit() or s[i-1] == ')'):
            stC.append('+')
        if s[i] == '-' and s[i-1] == '(':
            stN.append(newNode(0))
        stC.append(s[i])
        return i, False

    def handle_closing_bracket(self,stN: list, stC: list):
        while len(stC) != 0 and stC[-1] != '(':
            self.process_operator(stN, stC)
        stC.pop()

    def process_operator(self,stN: list, stC: list):
        t = newNode(stC[-1])
        stC.pop()
        if t.data in ('!', '~', '#'):
            t1 = stN.pop()
            t.right = t1
        else:
            try:
                t1 = stN.pop()
                t2 = stN.pop()
            except:
                raise MissingOperandError()
            t.left = t2
            t.right = t1
        stN.append(t)

    def validate_operator(self, s: str, i: int):
        if s[i] in ('#','!') and not(s[i-1].isdigit() or s[i-1] in ('#','!') or s[i-1] == ')'):
            if s[i] == '#':
                raise InvalidSumDigitsInputError(i-1)
            else:
                raise InvalidFactorialInputError(i-1)
        if s[i] == '~' and not(s[i+1].isdigit() or s[i+1] == '(' or s[i+1] == '-'):
            raise MissingNumberAfterTildeError(i+1)
        if ((6 > self.p[ord(s[i])] > 1) or s[i] == '+') and ((6 > self.p[ord(s[i-1])] > 1) or s[i-1] == '+'):
            raise ConsecutiveOperatorsError(i)

    def handle_double_minus(self, s: str, i: int, stN: list, stC: list) -> int:
        
        j = 0
        if s[i] == '~':
            j += 1
        while s[j+i] == '-':
            j += 1
        if not (s[j+i].isdigit() or s[i+j] == '('):
            raise MinusBeforeOperatorError(i+j)
        if j % 2 == 0:
            
            if s[i-1].isdigit():
                self.handle_operator(s, i+j-2, stN, stC)
                
                i , bol = self.handle_digits(s, i+j-1, False, stN, stC)
                return i
            #elif (s[i-1] == ')'):
            #   stC.append('+')
            
            i += j-1
        else:
            if s[i] == '~':
                stC.append('~')
                i += j-1
            else:
                if s[i-1] == '(':
                    stN.append(newNode(0))
                    self.handle_operator(s, i+j-2, stN, stC)
                    i += j-1
                elif (s[i-1] == ')'):
                    d = ['1','+','1']
                    self.handle_operator(d, 1, stN, stC)
                    i += j-2
                else:
                    
                    i += j-2
        return i

    def build(self,input: Istrable):
        s = "(" + input.getStr() + ")"
        stN = []
        stC = []
        
        

        i = 0
        two_digits_in_row = False
        while i < len(s):
            if s[i] == '(':
                stC.append(s[i])
            elif (s[i] == '-' and s[i+1] == '-') or (s[i] == '~' and s[i+1] == '-'):
                i = self.handle_double_minus(s, i, stN, stC)
            elif s[i].isdigit() or (s[i] == '-' and  ((6 > self.p[ord(s[i-1])] > 0) )):#and not s[i-1] == '-'
                i, two_digits_in_row = self.handle_digits(s, i, two_digits_in_row, stN, stC)
            elif self.p[ord(s[i])] > 0:
                i, two_digits_in_row = self.handle_operator(s, i, stN, stC)
            elif s[i] == ')':
                self.handle_closing_bracket(stN, stC)
                two_digits_in_row = False
            else:
                raise InvalidInputError(i)
            i += 1

        if len(stN) == 0:
            return newNode(0)
        if len(stN) != 1:
            raise MissingOperatorError()
        
        if len(stC) != 0:
            raise MissingCerlyBracketsError()
        
        return stN[-1]


        

