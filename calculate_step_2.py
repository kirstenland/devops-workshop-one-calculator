from calculate_sum import calculate_sum

def process_lines(lines):
    total = 0
    for line in lines:
        parts = line.split(" ")
        total += calculate_sum(parts[1], int(parts[2]), int(parts[3]))
    return total

with open("step_2.txt", "r") as f:
    lines = f.read().splitlines()
    print(process_lines(lines))
