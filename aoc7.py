from string import digits

rules = open('aoc7.txt').read().splitlines()
rules_dict = {'no other bag': []}
for rule in rules:
    bag_color, contents = rule.split(' contain ')
    bag_color = bag_color.rstrip('s')  # remove plural
    contents = contents.rstrip('.').split(', ')
    # remove any numbers from left, remove plural
    contents = [c.lstrip(digits).lstrip().rstrip('s')
                for c in contents]
    rules_dict[bag_color] = contents


def search(color):
    for new_color in rules_dict[color]:
        if new_color == 'shiny gold bag':
            return True
        if search(new_color):
            return True


t = sum(1 for color in rules_dict if search(color))
print(t)
