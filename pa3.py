import json
import sys
import time

def flatten_json(json_data):
    result = []
    processing_queue = [(json_data, 0)]
    current_index = 0

    while current_index < len(processing_queue):
        current_node, current_level = processing_queue[current_index]
        entry = {
            'level': current_level,
            'field1': current_node.get('field1'),
            'field2': current_node.get('field2')
        }

        if current_level > 0:
            result.append(entry)

        if current_node['nodes'] is not None:
            for child_node in current_node['nodes']:
                processing_queue.append((child_node, current_level + 1))
        current_index += 1

    return result

def main(input_file, output_file):
    with open(input_file, 'r') as json_file:
        json_data = json.load(json_file)

    start_time = time.time()

    flattened_data = flatten_json(json_data)

    end_time = time.time()
    runtime = end_time - start_time

    with open(output_file, 'w') as csv_file:
        csv_file.write("corresponding level, field1 value, field2 value\n")
        for entry in flattened_data:
            csv_file.write(f"{entry['level']}, {entry['field1']}, {entry['field2']}\n")

    print(f"Runtime: {runtime:.2f} seconds")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python pa3.py input.json output.csv")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        main(input_file, output_file)