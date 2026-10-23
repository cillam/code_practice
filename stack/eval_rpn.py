# Problem: Evaluate Reverse Polish Notation
# Difficulty: Medium
# Pattern:  (new one -- stack / LIFO)
# Time: O(n)  |  Space: O(n)
#
# Reverse Polish Notation (RPN) writes the operator AFTER its two operands,
# so "3 4 +" means 3 + 4 = 7, and "2 1 + 3 *" means (2 + 1) * 3 = 9.
#
# You're given `tokens`, a list of strings. Each token is either an integer
# (possibly negative, e.g. "-11") or one of the operators "+", "-", "*", "/".
# Evaluate the expression and return the result as an int.
#
# This is the textbook use of a STACK: push numbers as you see them; when you
# hit an operator, pop the two most recent numbers, combine them, and push the
# result back. At the end, the single value left on the stack is your answer.
#
# TWO gotchas to get right:
#   1. ORDER for '-' and '/'. The operands come off the stack most-recent
#      first. For "a b -" the result is a - b, so the number you pop FIRST is
#      the right-hand operand. Getting this backwards passes '+' and '*' (which
#      are commutative) but silently breaks '-' and '/'.
#   2. DIVISION truncates toward ZERO, not toward negative infinity. In Python,
#      -7 //  2 == -4  (floor)  <- NOT what you want
#       int(-7 / 2) == -3  (truncates toward zero)  <- this is what you want
#
# Examples:
#   eval_rpn(["2","1","+","3","*"])  -> 9
#   eval_rpn(["4","13","5","/","+"]) -> 6     # 4 + (13/5 = 2)
#   eval_rpn(["3","4","+"])          -> 7
#   eval_rpn(["-7","2","/"])         -> -3    # truncates toward zero, not -4
#   eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) -> 22

def eval_rpn(tokens):
    # pop from right-hand side. last in, first out
    answer_stack = []
    for token in tokens:
        if token.lstrip('-').isdigit():
            answer_stack.append(int(token))
        if token in ["*", "/", "+", "-"]:
            if token == "/":
                divisor = answer_stack.pop()
                dividend = answer_stack.pop()
                answer_stack.append(int(dividend/divisor))
            if token == "*":
                answer_stack.append(answer_stack.pop() * answer_stack.pop())
            if token == "+":
                answer_stack.append(answer_stack.pop() + answer_stack.pop())
            if token == "-":
                minus_num = answer_stack.pop()
                first_num = answer_stack.pop()
                answer_stack.append(first_num - minus_num)
    return answer_stack[0]


if __name__ == "__main__":
    assert eval_rpn(["2","1","+","3","*"]) == 9
    assert eval_rpn(["4","13","5","/","+"]) == 6
    assert eval_rpn(["3","4","+"]) == 7
    assert eval_rpn(["-7","2","/"]) == -3
    assert eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
    print("passed")
