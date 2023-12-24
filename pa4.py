#Estefania Perez
import csv
import sys

def process_input(input_filename):
    number_rows = {}

    with open(input_filename, 'r') as file:
        reader = csv.reader(file)
        for row_number, row in enumerate(reader, start=1):
            if row:  # Skip blank rows
                number = int(row[0])
                if number in number_rows:
                    number_rows[number].append(row_number)
                else:
                    number_rows[number] = [row_number]

    return number_rows

def write_output(output_filename, number_rows):
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        sorted_numbers = sorted(number_rows.items(), key=lambda x: len(x[1]), reverse=True)

        for number, rows in sorted_numbers:
            if len(rows) > 1:
                writer.writerow([number, len(rows)])

def main():
    if len(sys.argv) != 3:
        print("Usage: python pa4.py input_filename output_filename")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    number_rows = process_input(input_filename)
    write_output(output_filename, number_rows)

if __name__ == "__main__":
    main()