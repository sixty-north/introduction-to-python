RULE_30 = {
    '111': 0,
    '110': 0,
    '101': 0,
    '100': 1,
    '011': 1,
    '010': 1,
    '001': 1,
    '000': 0,
}

RULE_110 = {
    '111': 0,
    '110': 1,
    '101': 1,
    '100': 0,
    '011': 1,
    '010': 1,
    '001': 1,
    '000': 0,

}


def apply(rule, row):
    new_row = [0] * len(row)
    for i in range(1, len(row) - 1):
        new_row[i] = rule[''.join(map(str, row[i-1:i+2]))]
    return new_row


def generate_cells(rule, num_rows, num_columns):
    row = [0] * num_columns
    row[num_columns // 2] = 1
    for i in range(1, num_rows):
        yield row
        row = apply(rule, row)


def make_pixels(cells):
    return [
        [cell * 255 for cell in row]
        for row in cells]
