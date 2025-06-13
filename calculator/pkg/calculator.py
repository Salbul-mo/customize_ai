# calculator.py


class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        print("evaluate: " + str(expression))
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        result = self._evaluate_infix(tokens)
        print("evaluate result: " + str(result))
        return result

    def _evaluate_infix(self, tokens):
        print("_evaluate_infix: " + str(tokens))
        values = []
        operators = []

        for token in tokens:
            if token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    print("Before _apply_operator (while loop)")
                    self._apply_operator(operators, values)
                    print("After _apply_operator (while loop)")
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            print("Before _apply_operator (end)")
            self._apply_operator(operators, values)
            print("After _apply_operator (end)")

        if len(values) != 1:
            raise ValueError("invalid expression")

        print("_evaluate_infix result: " + str(values[0]))
        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))
