hw = open('aoc18.txt').read().splitlines()


def calc(expr):
    """ calculate expression from left to right
    ex) '2+4*9' = 6 * 9 = 54
    """
    if '(' in expr:
        end = expr.index(')')
        for i in range(end - 1, -1, -1):
            if expr[i] == '(':
                paren_expr = expr[i:end+1]
                return calc(expr.replace(paren_expr, calc(paren_expr[1:-1])))
    else:
        vals = expr.replace('+', ' ').replace('*', ' ').split()
        ops = [i for i in expr if i in '+*']
        ans = int(vals[0])
        for i in range(len(ops)):
            if ops[i] == '+':
                ans += int(vals[i + 1])
            else:
                ans *= int(vals[i + 1])
        return str(ans)


t = 0
for problem in hw:
    problem = problem.replace(' ', '')
    t += int(calc(problem))

print(t)
