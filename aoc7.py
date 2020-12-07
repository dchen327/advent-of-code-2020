from string import digits

rules = open('aoc7.txt').read().splitlines()
rules_dict1 = {'no other bag': []}
rules_dict2 = {'no other bag': []}
for rule in rules:
    bag_color, contents = rule.split(' contain ')
    bag_color = bag_color.rstrip('s')  # remove plural
    contents = contents.rstrip('.').split(', ')
    rules_dict2[bag_color] = contents
    # remove any numbers from left, remove plural
    contents = [c.lstrip(digits).lstrip().rstrip('s')
                for c in contents]
    rules_dict1[bag_color] = contents

# part 1


def search(color):
    for new_color in rules_dict1[color]:
        if new_color == 'shiny gold bag':
            return True
        if search(new_color):
            return True


t = sum(1 for color in rules_dict1 if search(color))
print(t)

# part 2
total_bags = 0


def search(color, num_color):
    global total_bags
    for new_color in rules_dict2[color]:
        if 'no other bag' in new_color:
            break
        num = int(new_color.split()[0])
        new_color = new_color.lstrip(digits).lstrip().rstrip('s')
        total_bags += num_color * num
        search(new_color, num_color * num)


search('shiny gold bag', 1)
print(total_bags)
