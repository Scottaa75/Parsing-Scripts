# import re

# def parse(input_file, output_file):
#     with open(input_file, 'r') as file:
#         file_content = file.read()
#         rule_pattern = r'RR-[^-\n]+ - Rule\]'
#         rule_content = re.compile(r'{}([\s\S]*?)(?=\n\n|$)'.format(rule_pattern))

#         matches = rule_content.finditer(file_content)

#         with open(output_file, 'w') as output:
#             for match in matches:
#                 output.write(f"\n{match.group(1)}\n\n")

# input_file = 'Es_all_search_final.txt'
# output_file = 'searches_output.txt'

# parse(input_file, output_file)

# import re

# def find_and_write_blocks(input_file, output_file):
#     with open(input_file, 'r') as file:
#         file_content = file.read()
#         block_pattern = re.compile(r'RR-[^-\n]+ - Rule\][\s\S]*?(?=\n\n|$)')

#         matches = block_pattern.finditer(file_content)

#         with open(output_file, 'w') as output:
#             for match in matches:
#                 output.write(f"\n{match.group(0)}\n")

# input_file = 'Es_all_search_final.txt'
# output_file = 'searches_output.txt'

# find_and_write_blocks(input_file, output_file)

# import re

# def parse(input_file, output_file):
#     with open(input_file, 'r') as file:
#         file_content = file.read()
#         rule_pattern = r'RR-[^-\n]+ - Rule\]'
#         rule_content = re.compile(r'{}([\s\S]*?)(?=\n\n|$)'.format(rule_pattern))
#         label_pattern = re.compile(r'action\.correlationsearch\.label\s*=\s*(.*?)\n')
#         search_pattern = re.compile(r'search\s*=\s*(.*?)\n')

#         matches = rule_content.finditer(file_content)

#         with open(output_file, 'w') as output:
#             for count, match in enumerate(matches, start=1):
#                 output.write(f"\n{count} {match.group(1)}\n")

#                 # Search for action.correlationsearch.label and write its value
#                 label_match = label_pattern.search(match.group(1))
#                 if label_match:
#                     output.write(f"  Label: {label_match.group(1)}\n")

#                 # Search for search = and write its value
#                 search_match = search_pattern.search(match.group(1))
#                 if search_match:
#                     output.write(f"  Search: {search_match.group(1)}\n")

# input_file = 'searches_output.txt'
# output_file = 'searches_output2.txt'

# parse(input_file, output_file)

import re

def parse(input_file, output_file):
    with open(input_file, 'r') as file:
        file_content = file.read()
        rule_pattern = r'RR-[^-\n]+ - Rule\]'
        rule_content = re.compile(r'{}([\s\S]*?)(?=\n\n|$)'.format(rule_pattern))
        label_pattern = re.compile(r'action\.correlationsearch\.label\s*=\s*(.*?)\n')
        search_pattern = re.compile(r'search\s*=\s*(.*?)\n')

        matches = rule_content.finditer(file_content)

        with open(output_file, 'w') as output:
            for count, match in enumerate(matches, start=1):
                output.write(f"\n{count}\n")

                # Search for action.correlationsearch.label and write its value within the code block
                label_match = label_pattern.search(match.group(1))
                if label_match:
                    output.write(f"  Label: {label_match.group(1)}\n")

                # Search for search = and write its value within the code block
                search_match = search_pattern.search(match.group(1))
                if search_match:
                    output.write(f"  Search: {search_match.group(1)}\n")

input_file = 'searches_output.txt'
output_file = 'searches_output2.txt'

parse(input_file, output_file)
