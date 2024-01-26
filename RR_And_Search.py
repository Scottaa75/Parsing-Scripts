import json

def convert_text_to_json(input_file_path, output_json_file_path, delimiter=','):
    try:
        with open(input_file_path, 'r') as input_file:
            lines = input_file.readlines()

            # Assuming the first line contains field names
            fields = lines[0].strip().split(delimiter)

            # Create a list to store the records
            records = []

            # Iterate through the lines to create records
            for line in lines[1:]:
                values = line.strip().split(" = ")
                record = dict(zip(fields, values))
                records.append(record)

            # Write the records to a JSON file
            with open(output_json_file_path, 'w') as output_json_file:
                json.dump(records, output_json_file, indent=2)
                print(f"JSON file '{output_json_file_path}' created successfully.")

    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")

# Example usage
input_file_path = "ES_all_search_final.txt"  # Replace with the path to your input text file
output_json_file_path = "output.json"  # Replace with the desired output JSON file path

convert_text_to_json(input_file_path, output_json_file_path)
