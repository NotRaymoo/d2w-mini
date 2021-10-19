

def mergesort(array, byfunc=None):
  if len(array) > 1:
        merge(array, 0, (len(array)-1) // 2, len(array)-1, byfunc)

def merge(array, p, q, r, byfunc=None):
    if r>p:
        merge(array, p, (p+q) // 2 , q, byfunc)
        merge(array, q+1, (q+1+r) // 2, r, byfunc)
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    n_left = len(left_array)
    n_right = len(right_array)
    left = 0
    right = 0
    dest = p
    while left < n_left and right < n_right:
        if byfunc is not None:
            a = byfunc(left_array[left])
            b = byfunc(right_array[right])
            if a <= b:
                array[dest] = left_array[left]
                left += 1
            else:
                array[dest] = right_array[right]
                right += 1
        elif left_array[left] <= right_array[right]:
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right += 1
        dest += 1
    while left < n_left:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right < n_right:
        array[dest] = right_array[right]
        right += 1
        dest += 1
        
class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop(-1) if not self.is_empty else None
            
    def peek(self):
        return None if self.is_empty else self.__items[-1]

    @property
    def is_empty(self):
        return self.size == 0

    @property
    def size(self):
        return len(self.__items)

class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    operand = '0123456789'
    operator = '+-*/()'
    def __init__(self, string=""):
        self.expression = string

    @property
    def expression(self):
        return self._expr

    @expression.setter
    def expression(self, new_expr):
        for i in new_expr:
            if i not in self.valid_char:
                self._expr = ""
                return
        self._expr = new_expr
    
    def insert_space(self):
        ls = [s for s in self.expression]
        prev_s = " "
        neg_num = False
        for i, s in enumerate(ls):
            if s in self.operator:
                if s == '-' and not prev_s in self.operand:
                    neg_num = True
                    ls[i] = ""
                else:
                    ls[i] = f" {ls[i]} "
            if neg_num and s in self.operand:
                ls[i] = prev_s+s
                neg_num = False
            if s!= " ":
                prev_s = s
        self.expression = ("").join(ls)
        return self.expression

    def process_operator(self, operand_stack, operator_stack):
        right = str(operand_stack.pop())
        left = str(operand_stack.pop())
        operator = operator_stack.pop()
        if operator == "/":
            operator = "//"
        operand_stack.push(eval(left+operator+right))  # from the previous parts

    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split()
        #print(tokens)
        # Add operands to stack
        for i, s in enumerate(tokens):
            if s == "+" or s == "-":
                while operator_stack.peek() != "(" and not operator_stack.is_empty:
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(s)
            elif s == "*" or s == "/":
                while operator_stack.peek() in ["*", "/"]:
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(s)
            elif s == "(":
                operator_stack.push(s)
            elif s == ")":
                while operator_stack.peek() != "(":
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.pop()
            else:
                operand_stack.push(s)
        while not operator_stack.is_empty:
            self.process_operator(operand_stack, operator_stack)
        return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]
