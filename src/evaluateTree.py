import math
from src.Exeptions import *

def evaluateExpressionTree(root):
 
    # empty tree
    if root is None:
        return 0
 
    # leaf node
    if root.left is None and root.right is None:
        return float(root.data)
 
    # evaluate left tree
    left_sum = evaluateExpressionTree(root.left)
 
    # evaluate right tree
    right_sum = evaluateExpressionTree(root.right)
 
    # check which operation to apply
    if root.data == '+':
        return left_sum + right_sum
 
    elif root.data == '-':
        if left_sum == 0 :
            return -right_sum
        elif right_sum == 0:
            return -left_sum
            
        return left_sum - right_sum
 
    elif root.data == '*':
        return left_sum * right_sum
 
    elif root.data == '/':
        return left_sum / right_sum
    elif root.data == '^':
        if left_sum < 0 and -1 < right_sum < 1:
            raise NegativeSqrtError()
        return math.pow(left_sum , right_sum)
    elif root.data == '%':
        return left_sum % right_sum
    elif root.data == '$':
        return max(left_sum,right_sum)
    elif root.data == '&':
        return min(left_sum,right_sum)
    elif root.data == '@':
        return (left_sum + right_sum) / 2
    elif root.data == '~':
        return -right_sum
    elif root.data == '!':
        return factorial(right_sum)
    elif root.data == '#':
        return sum_of_digits(right_sum)
    
 
 
def factorial(n):
    
    if n < 0:
        raise NegativeFactorialError()
    if n > 950:
        raise OverflowError()
    elif not isinstance(n, int) and not n.is_integer():
        raise FloatFactorialError()
    if (isinstance(n, float)) and n > 100:
        raise OverflowError()   
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


def sum_of_digits(n):
    if n < 0 :
        raise NegativeSumError()
    #if 'e' in str(n):
     #   raise OverflowError()
    return sum([int(i) for i in str(n) if i.isdigit()])