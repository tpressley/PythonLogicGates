class Gate(object):
    """Base class for any logic gate"""
    
    def eval():
        raise NotImplementedError("This function needs to be implemented")

    def __init__(self, **kwargs):
        self.a = bool
        self.q = bool
        return super().__init__(**kwargs)

class Two_Input_Gate(Gate):
    """Base class for any two-input gate"""

    def __init__(self, **kwargs):
        self.b = bool
        return super().__init__(**kwargs)


class TWO_IN_NAND(Two_Input_Gate):
    def eval(self):
        self.q = not (self.a and self.b)

class TWO_IN_NOR(Two_Input_Gate):
    def eval(self):
        self.q = not (self.a or self.b)

class TWO_IN_OR(Two_Input_Gate):
    def eval(self):
        self.q =  (self.a or self.b)

class TWO_IN_AND(Two_Input_Gate):
    def eval(self):
        self.q =  (self.a and self.b)

class TWO_IN_XOR(Two_Input_Gate):
    def eval(self):
        self.q = ((not self.a) and self.b) or (self.a and (not self.b))



class Three_Input_Gate(Two_Input_Gate):
    """Base class for any two-input gate"""

    def __init__(self, **kwargs):
        self.c = bool
        return super().__init__(**kwargs)


class THREE_IN_NAND(Three_Input_Gate):
    #'(ABC) = '((AB)(C))

    def eval(self):
        t = TWO_IN_AND()
        t.a = self.a
        t.b = self.b
        t.eval()
        t = t.q
        self.q = not (t and self.c)

class  THREE_IN_NOR(Three_Input_Gate):
    #'(A+B+C) = '((A+B)+C)
    def eval(self):
        t = TWO_IN_OR()
        t.a = self.a
        t.b = self.b
        t.eval()
        t = t.q
        self.q = not (t or self.c)

class   THREE_IN_OR(Three_Input_Gate):

    def eval(self):
        t = TWO_IN_OR()
        t.a = self.a
        t.b = self.b
        t.eval()
        t = t.q
        self.q =  (t or self.c)

class  THREE_IN_AND(Three_Input_Gate):
    
    def eval(self):
        t = TWO_IN_AND()
        t.a = self.a
        t.b = self.b
        t.eval()
        t = t.q
        self.q =  (t and self.c)

class  THREE_IN_XOR(Three_Input_Gate):
    def eval(self):
        t = TWO_IN_XOR()
        t.a = self.a
        t.b = self.b
        t.eval()
        t = t.q
        self.q = ((not t) and self.c) or (t and (not self.c))


