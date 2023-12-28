def get_data(file):
    with open(file) as f:
        return f.read().splitlines()


class ConditionReport:
    def __init__(self, condition_record, contiguous_group):
        self.condition_record = condition_record
        self.contiguous_group = contiguous_group


if __name__ == '__main__':
    data = get_data('2023/12/sample.txt')
    condition_records = [ConditionReport(*x.split()) for x in data]
    print(condition_records)
