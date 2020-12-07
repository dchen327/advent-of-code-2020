from string import digits

rules = open('aoc7.txt').read().splitlines()
rules_dict = {}
for rule in rules:
    bag, contents = rule.split(' contain ')
    bag = bag.rstrip('s')  # remove plural
    contents = contents.rstrip('.').split(', ')
    rules_dict[bag] = contents


t = 0
for color in rules_dict:
 # remove any numbers from left, remove plural
    contents = [c.lstrip(digits).lstrip().rstrip('s')
                for c in rules_dict[color]]
    contains_shiny_gold = False

    def search(color):
        global contains_shiny_gold
        contents = [c.lstrip(digits).lstrip().rstrip('s')
                    for c in rules_dict[color]]
        # print(contents)
        for new_color in contents:
            if new_color == 'shiny gold bag':
                contains_shiny_gold = True
                break
            elif new_color == 'no other bag':
                break
            else:
                search(new_color)

    search(color)
    if contains_shiny_gold:
        t += 1

print(t)
