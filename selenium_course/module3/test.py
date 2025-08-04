def process(input_string: str) -> str:
    below_zero = []
    zero = []
    more_zero = []
    numbers = [int(x) for x in input_string.split()]
    for i in numbers:
        if i < 0:
            below_zero.append(i)
        elif i == 0:
            zero.append(i)
        elif i > 0:
            more_zero.append(i)
    return f'выше нуля: {len(more_zero)}, ниже нуля: {len(below_zero)}, равна нулю: {len(zero)}'

input_string = input()
output_string = process(input_string)
print(output_string)