RULE_30 = [0, 1, 1, 1, 1, 0, 0, 0]
RULE_110 = [0, 1, 1, 1, 0, 1, 1, 0]


def apply(rule, row):
    new_row = [0] * len(row)
    triples = zip(row, row[1:], row[2:])
    for index, (a, b, c) in enumerate(triples):
        rule_index = (a << 2) + (b << 1) + c
        new_row[index + 1] = rule[rule_index]
    return new_row


def generate_cells(rule, num_rows, num_columns):
    row = [0] * num_columns
    for i in range(1, num_rows):
        yield row
        row = apply(rule, row)


def make_pixels(cells):
    return [
        [cell * 255 for cell in row]
        for row in cells]
