import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []

        ops = {
            "*":operator.mul,
            "+":operator.add,
            "-":operator.sub,
            "/":operator.truediv
        }

        for i in range(len(tokens)):
            if tokens[i] in ops:
                operation = tokens[i]
                if stk:
                    num1 = int(stk.pop())
                    num2 = int(stk.pop())
                stk.append(ops[operation](num2,num1))
            else:
                stk.append(tokens[i])
        return int(stk[-1])
                    
