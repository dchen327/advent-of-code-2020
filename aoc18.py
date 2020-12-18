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

# part 2


def calc2(expr):
    """ calculate expression from left to right, add before mul """
    if '(' in expr:
        end = expr.index(')')
        for i in range(end - 1, -1, -1):
            if expr[i] == '(':
                paren_expr = expr[i:end+1]
                return calc2(expr.replace(paren_expr, calc2(paren_expr[1:-1])))
    else:
        vals = expr.replace('+', ' ').replace('*', ' ').split()
        ops = [i for i in expr if i in '+*']
        for i in range(len(ops) - 1, -1, -1):
            if ops[i] == '+':
                s = int(vals[i]) + int(vals[i + 1])
                del vals[i + 1]
                del ops[i]
                vals[i] = str(s)
        prod = 1
        for i in vals:
            prod *= int(i)
        return str(prod)


t = 0
for problem in hw:
    problem = problem.replace(' ', '')
    t += int(calc2(problem))

print(t)
