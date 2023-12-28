import re


def get_data():
    with open('2023/03/input.txt') as f:
        return f.read().splitlines()


class PartNumber:
    def __init__(self, part_number, line_number, starting_position, data):
        self.part_number = part_number
        self.line_number = line_number
        self.starting_position = starting_position
        self.data = data

    @property
    def coordinates(self):
        return self.starting_position, self.line_number

    @property
    def length(self):
        return len(self.part_number)

    @property
    def values_below(self):
        try:
            return self.data[self.line_number + 1][self.starting_position:self.starting_position + self.length]
        except IndexError:
            return "."

    @property
    def values_above(self):
        try:
            return self.data[self.line_number - 1][self.starting_position:self.starting_position + self.length]
        except IndexError:
            return "."

    @property
    def values_left(self):
        try:
            return self.data[self.line_number][self.starting_position - 1]
        except IndexError:
            return "."

    @property
    def values_right(self):
        try:
            return self.data[self.line_number][self.starting_position + self.length]
        except IndexError:
            return "."

    @property
    def values_top_left(self):
        try:
            return self.data[self.line_number - 1][self.starting_position - 1]
        except IndexError:
            return "."

    @property
    def values_top_right(self):
        try:
            return self.data[self.line_number - 1][self.starting_position + self.length]
        except IndexError:
            return "."

    @property
    def values_bottom_left(self):
        try:
            return self.data[self.line_number + 1][self.starting_position - 1]
        except IndexError:
            return "."

    @property
    def values_bottom_right(self):
        try:
            return self.data[self.line_number + 1][self.starting_position + self.length]
        except IndexError:
            return "."

    @property
    def adjacent_values(self):
        values = self.values_below + self.values_above + self.values_left + self.values_right + self.values_top_left + self.values_top_right + self.values_bottom_left + self.values_bottom_right  # noqa
        return [v for v in values if v not in ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']]

    @property
    def has_adjacent_values(self):
        return len(self.adjacent_values) >= 1


def main(data):
    output = 0
    part_numbers = []
    for line_number, line_data in enumerate(data):
        for match in re.finditer(r'\d+', line_data):
            part_numbers.extend([PartNumber(match.group(), line_number, match.start(), data)])

    for part_number in part_numbers:
        if part_number.has_adjacent_values:
            output += int(part_number.part_number)
    return output

# ***** PART 2 *****


# class Gear:
#     def __init__(self, line_number, starting_position, data):
#         self.line_number = line_number
#         self.starting_position = starting_position
#         self.data = data

#     @property
#     def data_width(self):
#         return len(self.data[0])

#     @property
#     def data_height(self):
#         len(self.data)

#     @property
#     def coordinates(self):
#         return self.starting_position, self.line_number

#     @property
#     def value_above(self):
#         try:
#             return self.data[self.line_number - 1][self.starting_position]
#         except IndexError:
#             return

#     @property
#     def value_above_right(self):
#         try:
#             value = self.data[self.line_number - 1][self.starting_position + 1]
#             if re.match(r'\d', value):
#                 adjacent_value = value
#                 for x in range(self.starting_position + 2, self.data_width):
#                     if re.match(r'\d', self.data[self.line_number - 1][x]):
#                         adjacent_value += self.data[self.line_number - 1][x]
#                     elif self.data[self.line_number - 1][x] == '.':
#                         break
#                 return adjacent_value
#             else:
#                 return value
#         except IndexError:
#             return

#     @property
#     def value_right(self):
#         try:
#             value = self.data[self.line_number][self.starting_position + 1]
#             if re.match(r'\d', value):
#                 adjacent_value = value
#                 for x in range(self.starting_position + 2, self.data_width):
#                     if re.match(r'\d', self.data[self.line_number][x]):
#                         adjacent_value += self.data[self.line_number][x]
#                     elif self.data[self.line_number][x] == '.':
#                         break
#                 return adjacent_value
#             else:
#                 return value
#         except IndexError:
#             return

#     @property
#     def value_below_right(self):
#         try:
#             value = self.data[self.line_number + 1][self.starting_position + 1]
#             if re.match(r'\d', value):
#                 adjacent_value = value
#                 for x in range(self.starting_position + 2, self.data_width):
#                     if re.match(r'\d', self.data[self.line_number + 1][x]):
#                         adjacent_value += self.data[self.line_number + 1][x]
#                     elif self.data[self.line_number + 1][x] == '.':
#                         break
#                 return adjacent_value
#             else:
#                 return value
#         except IndexError:
#             return

#     @property
#     def value_below(self):
#         try:
#             return self.data[self.line_number + 1][self.starting_position]
#         except IndexError:
#             return

#     @property
#     def value_below_left(self):
#         try:
#             value = self.data[self.line_number + 1][self.starting_position - 1]
#             if re.match(r'\d', value):
#                 adjacent_value = value
#                 for x in range(self.starting_position - 2, 0, -1):
#                     if re.match(r'\d', self.data[self.line_number + 1][x]):
#                         adjacent_value = f"{self.data[self.line_number + 1][x]}{adjacent_value}"
#                     elif self.data[self.line_number + 1][x] == '.':
#                         break
#                 return adjacent_value
#             else:
#                 return value
#         except IndexError:
#             return

#     @property
#     def value_left(self):
#         try:
#             value = self.data[self.line_number][self.starting_position - 1]
#             if re.match(r'\d', value):
#                 adjacent_value = value
#                 for x in range(self.starting_position - 2, -1, -1):
#                     if re.match(r'\d', self.data[self.line_number][x]):
#                         adjacent_value = f"{self.data[self.line_number][x]}{adjacent_value}"
#                     elif self.data[self.line_number][x] == '.':
#                         break
#                 return adjacent_value
#             else:
#                 return value
#         except IndexError:
#             return

#     @property
#     def value_above_left(self):
#         try:
#             value = self.data[self.line_number - 1][self.starting_position - 1]
#             if re.match(r'\d', value):
#                 adjacent_value = value
#                 for x in range(self.starting_position - 2, -1, -1):
#                     if re.match(r'\d', self.data[self.line_number - 1][x]):
#                         adjacent_value = f"{self.data[self.line_number - 1][x]}{adjacent_value}"
#                     elif self.data[self.line_number - 1][x] == '.':
#                         break
#                 return adjacent_value
#             else:
#                 return value
#         except IndexError:
#             return

#     def show_output(self):
#         print(self.value_above_left, self.value_above, self.value_above_right)
#         print(self.value_left, '*', self.value_right)
#         print(self.value_below_left, self.value_below, self.value_below_right)

#     def get_output(self):
#         return f"""
#         {self.value_above_left}{self.value_above}{self.value_above_right}
#         {self.value_left}{'*'}{self.value_right}
#         {self.value_below_left}{self.value_below}{self.value_below_right}
#         """

#     def get_output_v2(self):

#         def fix(lst):
#             out = []
#             s1 = "".join(x for x in lst)
#             out.extend(s1.split('.'))
#             out = [x for x in out if x != '']
#             return out

#         output = fix([self.value_above_left, self.value_above, self.value_above_right])
#         output.extend(fix([self.value_left, '.', self.value_right]))
#         output.extend(fix([self.value_below_left, self.value_below, self.value_below_right]))

#         return output


if __name__ == '__main__':
    data = get_data()
    print(main(data))
