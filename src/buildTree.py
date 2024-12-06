from Istrable import *
from collection.tree import *

def build(input : Istrable):
    # Stack to hold nodes (tree)
    s = input.getStr()
    print(s)
    
    s = "(" + s
    s += ")"
    stN = []

    # Stack to hold operators
    stC = []

    # Prioritizing the operators
    p = [0] * 123
    p[ord('+')] = p[ord('-')] = 1
    p[ord('/')] = p[ord('*')] = 2
    p[ord('^')] = 3
    p[ord(')')] = 0

    i = 0
    while i < len(s):
        if s[i] == '(':
            # Push '(' in operator stack
            stC.append(s[i])
        elif s[i].isdigit() or (s[i] == '-' and i + 1 < len(s) and s[i + 1].isdigit()):
            # To handle multi-digit numbers, for example: "342"
            num = ''
            while i < len(s) and (s[i].isdigit() or s[i] == '.' or s[i] == ' '):
                if (s[i] == ' '):
                    i += 1
                    continue
                num += s[i]
                i += 1
            # Decrement the index as the outer loop increments it
            i -= 1
            t = newNode(int(num))
            stN.append(t)
        elif p[ord(s[i])] > 0:
            # If an operator with lower or same precedence appears
            while len(stC) != 0 and stC[-1] != '(' and \
                    ((s[i] != '^' and p[ord(stC[-1])] >= p[ord(s[i])]) or
                     (s[i] == '^' and p[ord(stC[-1])] > p[ord(s[i])])):

                # Get and remove the top element from the operator stack
                t = newNode(stC[-1])
                stC.pop()

                # Get and remove the top two nodes from the operand stack
                t1 = stN[-1]
                stN.pop()
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
            while len(stC) != 0 and stC[-1] != '(':
                t = newNode(stC[-1])
                stC.pop()
                t1 = stN[-1]
                stN.pop()
                t2 = stN[-1]
                stN.pop()
                t.left = t2
                t.right = t1
                stN.append(t)
            stC.pop()
        i += 1

    # The final tree root is the last remaining element in the operand stack
    return stN[-1]
 