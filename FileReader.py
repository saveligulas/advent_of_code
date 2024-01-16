def read_lines(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines


def read_line_with_spaces(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
    return lines
