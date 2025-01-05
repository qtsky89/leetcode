class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ret = []

        for op in operations:
            if op[0]=="-" or op.isdigit():
                ret.append(int(op))
            elif op == "C":
                ret.pop()
            elif op == "D":
                ret.append(ret[-1]*2)
            elif op == "+":
                ret.append(ret[-1] + ret[-2])
        
        return sum(ret)