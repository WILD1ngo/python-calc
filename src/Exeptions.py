class CalculatorError(Exception):
    """Base exception class for calculator errors"""
    def __init__(self, location=""):
        self.location = location
        super().__init__(f"{self.message}")
        if location != "":
            self.message = f"{self.message} at {location}"
        

class InvalidInputError(CalculatorError):
    """Exception raised for invalid input in calculations"""
    message = "Invalid input"
    def __init__(self, location=""):
        super().__init__(location)

class DivisionByZeroError(CalculatorError):
    """Exception raised when attempting to divide by zero"""
    message = "Division by zero is not allowed"
    def __init__(self, location=""):
        super().__init__(location)

class OverflowError(CalculatorError):
    """Exception raised when result exceeds maximum allowed value"""
    message = "Result exceeds maximum allowed value"
    def __init__(self, location=""):
        super().__init__(location)

class NegativeFactorialError(CalculatorError):
    """Exception raised when attempting factorial of a negative number"""
    message = "Cannot calculate factorial of a negative number"
    def __init__(self, location=""):
        super().__init__(location)

class FloatFactorialError(CalculatorError):
    """Exception raised when attempting factorial of a float number"""
    message = "Cannot calculate factorial of a float number"
    def __init__(self, location=""):
        super().__init__(location)

class NegativeSumError(CalculatorError):
    """Exception raised when sum of digits is negative"""
    message = "Sum of digits cannot be negative"
    def __init__(self, location=""):
        super().__init__(location)

class NegativeSqrtError(CalculatorError):
    """Exception raised when attempting square root of a negative number"""
    message = "Cannot calculate square root of a negative number"
    def __init__(self, location=""):
        super().__init__(location)

class MinusBeforeOperatorError(CalculatorError):
    """Exception raised when a minus sign appears directly before an operator"""
    message = "Minus sign cannot appear directly before an operator"
    def __init__(self, location=""):
        super().__init__(location)

class MissingOperatorError(CalculatorError):
    """Exception raised when an operator is missing between operands"""
    message = "Missing operator between operands"
    def __init__(self):
        super().__init__()

class InvalidFactorialInputError(CalculatorError):
    """Exception raised when factorial operator is used without a number before it"""
    message = "Number must appear before factorial operator"
    def __init__(self, location=""):
        super().__init__(location)
class InvalidSumDigitsInputError(CalculatorError):
    """Exception raised when sum of digits operator is used without a number before it"""
    message = "Number must appear before sum of digits operator"
    def __init__(self, location=""):
        super().__init__(location)

class MissingNumberAfterTildeError(CalculatorError):
    """Exception raised when tilde operator is used without a number after it"""
    message = "Number must appear after tilde operator"
    def __init__(self, location=""):
        super().__init__(location)

class MissingCerlyBracketsError(CalculatorError):
    """Exception raised when curly brackets are not properly paired"""
    message = "Missing curly brackets"
    def __init__(self, location=""):
        super().__init__(location)

class ConsecutiveOperatorsError(CalculatorError):
    """Exception raised when two operators appear consecutively"""
    message = "Cannot have two operators in a row"
    def __init__(self, location=""):
        super().__init__(location)

class MissingOperandError(CalculatorError):
    """Exception raised when an operand is missing"""
    message = "Missing operand in expression"
    def __init__(self, location=""):
        super().__init__(location)

class MissingNumberBeforeTildeError(CalculatorError):
    """Exception raised when tilde operator is operator before it"""
    message = "Operator must appear before tilde operator"
    def __init__(self, location=""):
        super().__init__(location)
