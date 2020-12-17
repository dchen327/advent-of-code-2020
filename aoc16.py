lines = open('aoc16.txt').read().split('\n\n')

rules, ticket, nearby_tickets = lines[0].split(
    '\n'), lines[1].split('\n')[-1], lines[2].split('\n')[1:]
my_ticket = list(map(int, ticket.split(',')))
nearby_tickets = [list(map(int, t.split(','))) for t in nearby_tickets]

rules_formatted = {}
for rule in rules:
    field = rule[:rule.index(':')]
    rule = rule[rule.index(':')+2:]
    rules_formatted[field] = rule

valid_tickets = []


def check_rule(rule, num):
    check = rule.replace('-', f' <= {num} <= ')
    return eval(check)


error_rate = 0
for nearby_ticket in nearby_tickets:
    valid = True
    for num in nearby_ticket:
        if not any(check_rule(rule, num) for rule in rules_formatted.values()):
            error_rate += num
            valid = False
    if valid:
        valid_tickets.append(nearby_ticket)

print(error_rate)

# part 2
field_to_idx = {field: list(range(len(rules_formatted)))
                for field in rules_formatted}
for ticket in valid_tickets:
    for i, num in enumerate(ticket):
        for field, idxs in field_to_idx.items():
            for idx in field_to_idx[field]:
                if not check_rule(rules_formatted[field], ticket[idx]):
                    idxs.remove(idx)

done = False
while not done:
    done = True
    for field, idxs in field_to_idx.items():
        if len(idxs) == 1:
            for field2, idxs2 in field_to_idx.items():
                if len(idxs2) > 1 and idxs[0] in idxs2:
                    idxs2.remove(idxs[0])
                    done = False

field_to_idx = {field: idxs[0] for field, idxs in field_to_idx.items()}
prod = 1
for field in field_to_idx:
    if field[:9] == 'departure':
        prod *= my_ticket[field_to_idx[field]]

print(prod)
