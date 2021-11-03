class Calculator:

    def run(self):
        expression = self.read_expression()
        l = self.expression_to_list(expression)
        p = self.list_to_postscript(l)
        print(self.postscript_calculator(p))

    @staticmethod
    def read_expression():
        return input("Input Math expression\n")

    @staticmethod
    def expression_to_list(expression: str):
        l = expression.split()
        return l

    @staticmethod
    def postscript_calculator(postscrip_list: list):
        stack = []
        for symbol in postscrip_list:
            if symbol.isnumeric():
                stack.append(float(symbol))
            else:
                match symbol:
                    case "+":
                        stack[-2] = stack[-2] + stack[-1]
                    case "-":
                        stack[-2] = stack[-2] - stack[-1]
                    case "*":
                        stack[-2] = stack[-2] * stack[-1]
                    case "/":
                        stack[-2] = stack[-2] / stack[-1]
                    case "**":
                        stack[-2] = stack[-2] ** stack[-1]
                    case "%":
                        stack[-2] = stack[-2] % stack[-1]
                stack.pop(-1)

        return stack

    @staticmethod
    def list_to_postscript(expression_list:list):
        postscript = []
        operators = []
        priority = []
        for symbol in expression_list:
            if symbol.isnumeric():
                postscript.append(symbol)
            else:
                match symbol:
                    case "+":
                        if len(operators) == 0:
                            operators.append("+")
                            priority.append(0)
                        else:
                            while priority[-1]>0:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("+")
                            priority.append(0)
                    case "-":
                        if len(operators) == 0:
                            operators.append("-")
                            priority.append(0)
                        else:
                            while priority[-1] > 0:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("-")
                            priority.append(0)
                    case "*":
                        if len(operators) == 0:
                            operators.append("*")
                            priority.append(1)
                        else:
                            while priority[-1] > 1:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("*")
                            priority.append(1)
                    case "/":
                        if len(operators) == 0:
                            operators.append("/")
                            priority.append(1)
                        else:
                            while priority[-1] > 1:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("/")
                            priority.append(1)
                    case "%":
                        if len(operators) == 0:
                            operators.append("%")
                            priority.append(1)
                        else:
                            while priority[-1] > 1:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("%")
                            priority.append(1)
                    case "**":
                        if len(operators) == 0:
                            operators.append("**")
                            priority.append(2)
                        else:
                            while priority[-1] > 2:
                                postscript.append(operators.pop())
                                priority.pop()
                                if len(priority) == 0:
                                    break
                            operators.append("**")
                            priority.append(2)
                    case "(":
                        operators.append("(")
                        priority.append(-1)
                    case ")":
                        while priority[-1] != -1:
                            postscript.append(operators.pop())
                            priority.pop()
                        priority.pop()
                        operators.pop()
                    case _:
                        return  None

        while len(operators) > 0:
            postscript.append(operators.pop(-1))
        print(postscript)
        return postscript

    @staticmethod
    def print_result(stack):
        if stack is None:
            print()
