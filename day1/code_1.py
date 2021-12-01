previous_line = -1
increased_amount = 0

with open("input.txt", "r") as input_file:
    input_lines = input_file.readlines()

    for input_line in input_lines:
        input_line = int(input_line)
        difference_string = "N/A - no previous measurement"

        if previous_line > 0:
            if input_line > previous_line:
                difference_string = "increased"
                increased_amount += 1
            elif input_line < previous_line:
                difference_string = "decreased"
            else:
                difference_string = "no difference"

        print(f"{input_line} ({difference_string})")
        previous_line = input_line

print(f"\nIncreased amount: {increased_amount}")