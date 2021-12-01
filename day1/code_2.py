import numpy.lib.stride_tricks

input_file = numpy.loadtxt("input.txt")
sliding_window = numpy.lib.stride_tricks.sliding_window_view(input_file, 3)

previous_slide = -1
increased_amount = 0

for single_slide in sliding_window:
    sum_slide = sum(single_slide)
    difference_string = "N/A - no previous measurement"

    if previous_slide > 0:
        if sum_slide > previous_slide:
            difference_string = "increased"
            increased_amount += 1
        elif sum_slide < previous_slide:
            difference_string = "decreased"
        else:
            difference_string = "no difference"

    print(f"{sum_slide} ({difference_string})")
    previous_slide = sum_slide

print(f"\nIncreased amount: {increased_amount}")