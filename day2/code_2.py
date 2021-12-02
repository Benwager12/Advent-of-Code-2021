input_lines = open("input.txt", "r").read().split("\n")

# [horizontal, depth]
positioning = [0, 0]
aim = 0

for current_line in input_lines:
    command = current_line.split(" ")[0]
    instruction = int(" ".join(current_line.split(" ")[1::]))

    if command == "forward":
        positioning[0] += instruction
        positioning[1] += instruction * aim
    elif command == "down":
        aim += instruction
    elif command == "up":
        aim -= instruction

print(positioning[0] * positioning[1])