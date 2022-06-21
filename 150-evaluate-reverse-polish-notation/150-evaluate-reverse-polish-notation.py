class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        will you need to use truncation from an import or something?
        
        for * and / , you know that there will be 2 operands, so go back two and do that operation between those nums
        """
        operators = "+-*/"
        sta = []
        for token in tokens:
            if token in operators:
                operand_2 = sta.pop()
                operand_1 = sta.pop()
                evaluated = eval(f"{operand_1}{token}{operand_2}")
                sta.append(math.trunc(evaluated))
            else:
                sta.append(int(token))
        return sta[0]