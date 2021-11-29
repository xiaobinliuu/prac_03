def main():
    INPUT_FILE = 'temps_input.txt'
    OUTPUT_FILE = 'temps_output.txt'
    input_file = open(INPUT_FILE, 'r')
    output_file = open(OUTPUT_FILE, 'w')
    for line in input_file:
        convert_number = convert_temps(float(line))
        print(format(convert_number), file=output_file)
    input_file.close()
    output_file.close()


def convert_temps(convert_number):
    return (convert_number + 32) / 1.8


main()
