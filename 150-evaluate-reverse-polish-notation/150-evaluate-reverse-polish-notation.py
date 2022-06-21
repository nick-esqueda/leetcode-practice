class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        for * and / , you know that there will be 2 operands, so go back two and do that operation between those nums
        """
        # operators = "+-*/"
        # sta = []
        # for token in tokens:
        #     if token in operators:
        #         operand_2 = sta.pop()
        #         operand_1 = sta.pop()
        #         evaluated = eval(f"{operand_1}{token}{operand_2}")
        #         sta.append(math.trunc(evaluated))
        #     else:
        #         sta.append(int(token))
        # return sta[0]
        
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]