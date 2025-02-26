import re
from re import Pattern
from abc import ABC, abstractmethod

tokens_re: Pattern = re.compile(
    r"[a-z][a-z0-9]*"
    r"|-?[0-9]+"
    r"|[()]"
)

reserved_words = {
        "let": "LET",
        "add": "ADD",
        "mult": "MULT",
        "EOS": "EOS"
    }

symbols = {
        "(": "LPAREN",
        ")": "RPAREN"
    }

class Token:
    def __init__(self, tkn):
        self.string = tkn
        self.value = tkn

        if tkn.isdigit() or (tkn[0] == "-" and tkn[1:].isdigit()):
            self.kind = "INT"
            self.value = int(tkn)
        elif tkn.isalnum():
            self.spelling = tkn
            if tkn in reserved_words:
                self.kind = reserved_words[tkn]
            else:
                self.kind = "ID"
        elif tkn in symbols:
            self.kind = symbols[tkn]
        else:
            print("Illegal symbol", self.kind)

class Scanner:
    def __init__(self, expression: str):
        self._source = expression
        self._tokens = tokens_re.findall(self._source)
        self.current = None
        self.advance()

    def _next_token(self):
        if self.current != "EOS":
            tkn = self._tokens.pop(0)
            return Token(tkn)
        return None

    def has_more(self) -> bool:
        return len(self._tokens) > 0
    
    def advance(self):
        if self.has_more:
            self.current = self._next_token()

    def match(self, expected):
        val = self.current.value
        if self.current.kind != expected:
            print(f"Expected {expected}, got {self.current.string}")
        self.advance()
        return val

class PtNode(ABC):
    def __init__(self, name: str, children = None):
        self.name = name
        if children is not None:
            self.children = children
        else:
            self.children = []

    @abstractmethod
    def accept(self, visitor) -> None:
        pass

class LetNode(PtNode):
    def accept(self, visitor):
        return visitor.visit_let_expr(self)
    
class AddNode(PtNode):
    def accept(self, visitor):
        return visitor.visit_add_expr(self)
    
class MultNode(PtNode):
    def accept(self, visitor):
        return visitor.visit_mult_expr(self)
    
class IdNode(PtNode):
    def accept(self, visitor):
        return visitor.visit_id_expr(self)
    
class NumNode(PtNode):
    def accept(self, visitor):
        return visitor.visit_num_expr(self)
    
class Visitor(ABC):
    @abstractmethod
    def visit_let_expr(self, expr: LetNode):
        pass

    @abstractmethod
    def visit_add_expr(self, expr: LetNode):
        pass

    @abstractmethod
    def visit_mult_expr(self, expr: LetNode):
        pass

    @abstractmethod
    def visit_id_expr(self, expr: LetNode):
        pass

    @abstractmethod
    def visit_num_expr(self, expr: LetNode):
        pass
    
class Parser:
    def __init__(self, tokens):
        self._current = 0
        self._tokens: list[Token] = tokens

    def parse(self):
        tree = self._parse_expr()
        return tree
    
    def _parse_expr(self):
        if self._current >= len(self._tokens):
            return None
        if self._tokens[self._current].kind == "LPAREN":
            self._consume("LPAREN")
        match self._tokens[self._current].kind:
            case "LET":
                return self._parse_let()
            case "ADD":
                return self._parse_add()
            case "MULT":
                return self._parse_mult()
            case _:
                return self._parse_variable()
            
    def _parse_variable(self):
        if self._tokens[self._current].kind == "ID":
            return self._parse_id()
        return self._parse_int()
    
    def _parse_int(self):
        num = self._consume("INT")
        return NumNode("INT", [num])
    
    def _parse_id(self):
        id = self._tokens[self._current]
        self._consume("ID")
        return IdNode(id.string)
    
    def _parse_let(self):
        self._consume("LET")
        children = []
        while self._tokens[self._current].kind != "RPAREN" and self._tokens[self._current].kind != "EOS":
           children.append(self._parse_expr()) 
        self._consume("RPAREN", "EOS")
        return LetNode("LET", children)
    
    def _parse_add(self):
        self._consume("ADD")
        lhs = self._parse_expr()
        rhs = self._parse_expr()
        self._consume("RPAREN", "EOS")
        return AddNode("ADD", [lhs, rhs])
    
    def _parse_mult(self):
        self._consume("MULT")
        lhs = self._parse_expr()
        rhs = self._parse_expr()
        self._consume("RPAREN", "EOS")
        return MultNode("MULT", [lhs, rhs])


    def _consume(self, *expected):
        if self._tokens[self._current].kind not in set(expected):
            print(f"Expected {expected}, got {self._tokens[self._current].kind}, current={self._current}")
        self._current += 1
        return self._tokens[self._current - 1]

class Interpreter(Visitor):
    def __init__(self):
        super().__init__()
        self._environment = {}

    def _lookup_name(self, name: str) -> int:
        env = self._environment
        while env is not None:
            if (val := env.get(name)) is not None:
                return val
            env = env.get("!enclosing")
        return None

    def visit_let_expr(self, expr: LetNode):
        self._environment = { "!enclosing": self._environment}
        if len(expr.children) == 2: # special case
            name = expr.children[0].name
            sub_expr = expr.children[1]
            res = sub_expr.accept(self)
            self._environment[name] = res
        else:
            it = iter(expr.children)
            sub_exprs = [ (a, b) if b is not None else a for a, b in zip(it, it)]
            for i in range(len(sub_exprs)):
                sub_expr = sub_exprs[i]
                name = sub_expr[0].name
                res = sub_expr[1].accept(self)
                self._environment[name] = res
            last = expr.children[-1]
            res = last.accept(self)
        self._environment = self._environment["!enclosing"]
        return res

    
    def visit_add_expr(self, expr: AddNode) -> int:
        lhs, rhs = expr.children
        lhs = lhs.accept(self)
        rhs = rhs.accept(self)
        return lhs + rhs
    
    def visit_mult_expr(self, expr: MultNode):
        lhs, rhs = expr.children
        lhs = lhs.accept(self)
        rhs = rhs.accept(self)
        return lhs * rhs

    def visit_id_expr(self, expr: IdNode):
        return self._lookup_name(expr.name)
    
    def visit_num_expr(self, expr: NumNode) -> int:
        return expr.children[0].value
    

class Solution:
    def evaluate(self, expression: str) -> int:
        scanner = Scanner(expression)
        tokens = []
        while scanner.has_more():
            tokens.append(scanner.current)
            scanner.advance()
        tokens.append(Token("EOS"))
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        res = ast.accept(interpreter)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.evaluate("(mult 2 (add 4 3))")) # 14
    print(s.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))")) # 14
    print(s.evaluate("(let x 3 x 2 x)")) # 2
    print(s.evaluate("(let x 1 y 2 x (add x y) (add x y))")) # 5
    print(s.evaluate("(let a1 3 b2 (add a1 1) b2)")) # 4
    print(s.evaluate("(let x 7 -12)")) # -12