import math


def evaluateExpressionTree(root):
 
    # empty tree
    if root is None:
        return 0
 
    # leaf node
    if root.left is None and root.right is None:
        return int(root.data)
 
    # evaluate left tree
    left_sum = evaluateExpressionTree(root.left)
 
    # evaluate right tree
    right_sum = evaluateExpressionTree(root.right)
 
    # check which operation to apply
    if root.data == '+':
        return left_sum + right_sum
 
    elif root.data == '-':
        return left_sum - right_sum
 
    elif root.data == '*':
        return left_sum * right_sum
 
    elif root.data == '/':
        return left_sum / right_sum
    elif root.data == '^':
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
        return -left_sum
    elif root.data == '!':
        return factorial(right_sum)
    
 
 
 
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)