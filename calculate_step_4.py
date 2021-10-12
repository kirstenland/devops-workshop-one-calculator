from calculate_sum import calculate_sum

def process_goto(parts):
    if parts[1] == "calc":
        current_line_number = int(calculate_sum(parts[2], int(parts[3]), int(parts[4]))) - 1
    else:
        current_line_number = int(parts[1]) - 1
    return current_line_number

def process_remove(current_lines, current_line_number, parts):
    line_to_remove = int(parts[1]) - 1
    if 0 <= line_to_remove < len(current_lines):
        del current_lines[line_to_remove]
    if 0 <= line_to_remove <= current_line_number:
        return current_line_number
    else:
        return current_line_number + 1

def process_replace(current_lines, current_line_number, parts):
    line_to_replace = int(parts[1]) - 1
    line_to_replace_with = int(parts[2]) - 1
    if 0 <= line_to_replace < len(current_lines) and 0 <= line_to_replace_with < len(current_lines):
        current_lines[line_to_replace] = current_lines[line_to_replace_with]
    return current_line_number + 1


def process_lines(lines):
    current_lines = lines.copy()
    current_line_number = 0
    seen_lines = set()
    while not current_lines[current_line_number] in seen_lines :
        line = current_lines[current_line_number]
        print(current_line_number + 1, line)
        seen_lines.add(line)

        parts = line.split(" ")
        instruction = parts[0]

        if instruction == "goto":
            current_line_number = process_goto(parts)
        elif instruction == "remove":
            current_line_number = process_remove(current_lines, current_line_number, parts)
        elif instruction == "replace":
            current_line_number = process_replace(current_lines, current_line_number, parts)
    return (current_line_number + 1, current_lines[current_line_number])

with open("step_4.txt", "r") as f:
    lines = f.read().splitlines()
    print(process_lines(lines))
