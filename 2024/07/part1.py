def parse_file(filename: str):
    with open(filename) as f:
        lines = f.read().splitlines()
    return process_lines(lines)


def process_lines(lines: list) -> list:
    equations = []
    for i, line in enumerate(lines):
        test_value, numbers = line.split(":")
        test_value = int(test_value)
        numbers = [int(n) for n in numbers.strip().split()]
        equations.append(
            {
                test_value: numbers,
            }
        )
    return equations


def evaluate_expression(numbers: list, operators: list) -> tuple[int, str]:
    result = numbers[0]
    expr = str(numbers[0])

    for i in range(len(operators)):
        expr += f" {operators[i]} {numbers[i + 1]}"
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        else:
            raise ValueError(f"{operators[i]} is not a valid operator")
    return result, expr


def generate_all_operator_combinations(n: int) -> list:
    if n <= 1:
        return [[]]
    combinations = []
    for operators in generate_all_operator_combinations(n-1):
        combinations.append(operators + ['+'])
        combinations.append(operators + ['*'])
    return combinations


def can_make_target(target: int, numbers: list) -> tuple[bool, str]:
    operator_combinations = generate_all_operator_combinations(len(numbers))
    for operators in operator_combinations:
        result, expr = evaluate_expression(numbers, operators)
        if result == target:
            return True, expr
    return False, ""


def main() -> int:
    # equations = parse_file("2024/07/example2.txt")
    equations = parse_file("2024/07/input.txt")
    answer = 0
    for equation in equations:
        for target, numbers in equation.items():
            result, expr = can_make_target(target, numbers)
            if result:
                print(f"Found {expr} = {target}")
                answer += target
            else:
                print(f"No Result = {target}")
    return answer


if __name__ == '__main__':
    print(main())
