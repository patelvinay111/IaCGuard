import json


def import_gen(file_path):
    # Open the file for reading
    with open(file_path, 'r') as file:
        # Load the JSON data from the file
        json_data = json.load(file)

    grouped_data = {}

    # Group items based on type
    for item in json_data:
        item_type = item['type']
        if item_type not in grouped_data:
            grouped_data[item_type] = []
        grouped_data[item_type].append(item)

    # Now 'grouped_data' is a dictionary where keys are types, and values are lists of items for that type
    # For example: {'aws_internet_gateway': [...], 'aws_instance': [...]}

    output_path = file_path.split('.', 1)[0] + '_import_blocks.tf'
    with open(output_path, 'w') as file:
        # Print the resulting arrays
        for array in grouped_data.values():
            for idx, i in enumerate(array):
                s = ('import {\n\t' +
                     'id = "' + i['id'] + '"\n\t' +
                     'to = ' + i['type'] + '.' + str(idx) + '\n' +
                     '}\n\n'
                     )
                file.write(s)
    return output_path
