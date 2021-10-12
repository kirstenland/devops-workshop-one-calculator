from calculate_sum import calculate_sum

def process_lines(lines):
    current_line_number = 0
    seen_lines = set()
    while not lines[current_line_number] in seen_lines :
        line = lines[current_line_number]
        #print(current_line_number + 1, line)
        seen_lines.add(line)
        parts = line.split(" ")
        if parts[1] == "calc":
            current_line_number = int(calculate_sum(parts[2], int(parts[3]), int(parts[4]))) - 1
        else:
            current_line_number = int(parts[1]) - 1
    #print(current_line_number + 1, lines[current_line_number])
    return (current_line_number + 1, lines[current_line_number])

with open("step_3.txt", "r") as f:
    lines = f.read().splitlines()
    print(process_lines(lines))
