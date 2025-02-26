from functools import reduce

class PtNode:
    def __init__(self, type: str, children: list = None):
        self.type = type
        self.children = [] if children is None else children

    def visit(self) -> bool:
        if self.type == "f":
            return False
        if self.type == "t":
            return True
        # evaluate children
        operands = list(map(lambda child: child.visit(), self.children))
        if self.type == "or":
            return reduce(lambda lhs, rhs: lhs or rhs, operands)
        if self.type == "and":
            return reduce(lambda lhs, rhs: lhs and rhs, operands)
        if self.type == "not":
            # NOT expr will have exactly one child
            return not operands[0]
        print("Reached the unreachable")

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        root, _ = self.parse_expr(expression, 0)
        return root.visit()

    def parse_expr(self, expression: str, i: int) -> tuple[PtNode, int]:
        match expression[i]:
            case "f": return PtNode("f"), i + 1
            case "t": return PtNode("t"), i + 1
            case "!": type = "not"
            case "|": type = "or"
            case "&": type = "and"
        node = PtNode(type, [])
        i += 2  # consume operator and opening bracket
        while i < len(expression):
            if expression[i] == ")":
                return node, i
            elif expression[i] in { "!", "&", "|" }:
                child, next_idx = self.parse_expr(expression, i)
                node.children.append(child)
                i = next_idx + 1
            elif expression[i] == ",":
                i += 1
            elif expression[i] == "t":
                node.children.append(PtNode("t", []))
                i += 1
            elif expression[i] == "f":
                node.children.append(PtNode("f", []))
                i += 1
        return node, -1



if __name__ == "__main__":
    s = Solution()
    print(s.parseBoolExpr("&(|(f))"))
    print(s.parseBoolExpr("|(f,f,f,t)"))
    print(s.parseBoolExpr("!(&(f,t))"))
    print(s.parseBoolExpr("!(&(&(!(&(f)),&(t),|(f,f,t)),&(t),&(t,t,f)))"))
