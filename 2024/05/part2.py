from collections import defaultdict


def parse_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return split_input(lines)


def split_input(lines):
    index = lines.index("")
    return lines[:index], lines[index + 1:]


def create_rules_dict(rules):
    rules_dict = defaultdict(list)
    for rule in rules:
        a, b = rule.split('|')
        rules_dict[int(a)].append(int(b))
    return rules_dict


def get_middle_element_of_list(input_list):
    return input_list[len(input_list) // 2]


def correctly_ordered(page_numbers, rules_dict):
    return all([set(page_numbers[page_index+1:]).issubset(rules_dict[page_num])
                for page_index, page_num in enumerate(page_numbers)])


def reorder(lst, rules_dict):
    output = []
    for element in lst:
        for i, e in enumerate(output):
            if e in rules_dict[element]:
                output.insert(i, element)
                break
        else:
            output.append(element)
    return output


def main():
    # rules, page_numbers = parse_file("2024/05/example.txt")
    rules, page_numbers = parse_file("2024/05/input.txt")
    page_numbers = [[int(p) for p in pages.split(",")] for pages in page_numbers]
    rules_dict = create_rules_dict(rules)
    answer = 0
    for page_number in page_numbers:
        if not correctly_ordered(page_number, rules_dict):
            reordered = reorder(page_number, rules_dict)
            answer += get_middle_element_of_list(reordered)
    return answer


if __name__ == '__main__':
    print(main())
