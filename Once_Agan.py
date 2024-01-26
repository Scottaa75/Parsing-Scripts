# import re

# def parse(input_file, output_file):

#     with open(input_file, 'r') as file:
#         file_content = file.read()
#         rule_pattern = r'RR-[^-]+ - Rule\]'
#         rule_content = re.compile(r'{}([\s\S]*?){}'.format(rule_pattern, rule_pattern))

#         matches = rule_content.finditer(file_content)

#         with open(output_file, 'w') as output:
#             for match in matches:
#                 rules = re.findall(r'RR-[^-]+ - Rule\]', match.group(1))
                
#                 for count, rule in enumerate(rules, start=1):
#                     output.write(f"\n{count} [{rule}]\n")

# input_file = 'savedsearches_OC1.txt'
# output_file = 'searches_output.txt'

# parse(input_file, output_file)

import re

def parse(input_file, output_file):

    with open(input_file, 'r') as file:
        file_content = file.read()
        rule_pattern = r'RR-[^-]+ - Rule\]'
        rule_content = re.compile(r'{}([\s\S]*?){}'.format(rule_pattern, rule_pattern))

        matches = rule_content.finditer(file_content)

        with open(output_file, 'w') as output:
            for match in matches:
                rules = re.findall(r'RR-[^-]+ - Rule\]', match.group(1))
                
                for count, rule in enumerate(rules, start=1):
                    output.write(f"\n{count} [{rule}]\n")

input_file = 'savedsearches_OC1.txt'
output_file = 'searches_output.txt'

parse(input_file, output_file)