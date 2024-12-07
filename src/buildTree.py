from Istrable import *
from collection.tree import *

def build(input : Istrable):
    
    s = input.getStr()
    
    
    s = "(" + s
    s += ")"
    # Stack to hold nodes (tree)
    stN = []

    # Stack to hold operators
    stC = []

    # Prioritizing the operators
    p = [0] * 127
    p[ord('+')] = p[ord('-')] = 1
    p[ord('/')] = p[ord('*')] = 2
    p[ord('^')] = 3
    p[ord('%')] = 4
    p[ord('$')] = p[ord('@')] =  p[ord('&')] = 5
    p[ord('~')] = p[ord('!')] = 6
    p[ord(')')] = 0

    i = 0
    two_digits_in_row = False
    while i < len(s):
        
        if s[i] == '(':
            # Push '(' in operator stack
            stC.append(s[i])
        elif (s[i] == '-' and s[i+1] == '-'):
            i += 1
            
        elif s[i].isdigit() or (s[i] == '-' and s[i+1].isdigit()):
            # To handle multi-digit numbers, for example: "342"
            if two_digits_in_row:
                stC.append('+')
            two_digits_in_row = True
            num = ""
            if (s[i] == '-'):
                num += '-'
                #stC.append('+')
                i += 1
            while i < len(s) and (s[i].isdigit() or s[i] == '.' or s[i] == ' '):
                if (s[i] == ' '):
                    i += 1
                    continue

                num += s[i]
                i += 1
            # Decrement the index as the outer loop increments it
            
            i -= 1
            t = newNode(float(num))
            stN.append(t)
        elif p[ord(s[i])] > 0:
            two_digits_in_row = False
            # If an operator with lower or same precedence appears
            while len(stC) != 0 and stC[-1] != '(' and \
                    ((s[i] != '^' and p[ord(stC[-1])] >= p[ord(s[i])]) or
                     (s[i] == '^' and p[ord(stC[-1])] > p[ord(s[i])])):

                # Get and remove the top element from the operator stack
                t = newNode(stC[-1])
                
                
                stC.pop()
                if (t.data == '~' or t.data == '!' or t.data == '-'):
                    t1 = stN[-1]
                    stN.pop()
                    t.right = t1
                    stN.append(t)
                    
                # Get and remove the top two nodes from the operand stack
                else:
                    t1 = stN[-1]
                    stN.pop()
                    
                    #if stN.empty():
                        
                    t2 = stN[-1]
                    
                    stN.pop()
                    # Update the tree
                    t.left = t2
                    t.right = t1

                    # Push the tree back to the operand stack
                    stN.append(t)

            # Push current operator to operator stack
            stC.append(s[i])

        elif s[i] == ')':
            two_digits_in_row = False
            if len(stC) == 1:
                raise Exception("Error dont have '('\n", i)
            while len(stC) != 0 and stC[-1] != '(':
                t = newNode(stC[-1])
                stC.pop()
                if (t.data == '!'):
                    
                    t1 = stN[-1]
                    stN.pop()
                    t.right = t1
                    stN.append(t)
                elif(t.data == '~'):
                    t1 = stN[-1]
                    stN.pop()
                    t.left = t1
                    stN.append(t)
                else:    
                    t1 = stN[-1]
                    stN.pop()
                    t2 = stN[-1]
                    stN.pop()
                    t.left = t2
                    t.right = t1
                    stN.append(t)
            stC.pop()
        elif s[i].isspace():
            i += 1
        else:
            raise Exception("invalid input (Only accsept numbers and operators) \n", i)

            
        i += 1

    # The final tree root is the last remaining element in the operand stack
    return stN[-1]
 