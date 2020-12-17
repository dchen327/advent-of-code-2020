lines = open('aoc16.txt').read().split('\n\n')

rules, ticket, nearby_tickets = lines[0].split(
    '\n'), lines[1].split('\n')[-1], lines[2].split('\n')[1:]
ticket = list(map(int, ticket.split(',')))
nearby_tickets = [list(map(int, t.split(','))) for t in nearby_tickets]
rules_formatted = []
for rule in rules:
    rule = rule[rule.index(':')+2:]
    # p1, p2 = rule.split(' or ')
    # rules_formatted.append(p1)
    # rules_formatted.append(p2)
    rules_formatted.append(rule)


def check_rule(rule, num):
    check = rule.replace('-', f' <= {num} <= ')
    return eval(check)


error_rate = 0
for nearby_ticket in nearby_tickets:
    for num in nearby_ticket:
        if not any(check_rule(rule, num) for rule in rules_formatted):
            error_rate += num

print(error_rate)
