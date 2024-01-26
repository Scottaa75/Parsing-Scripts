# # import re

# # def find_search_lines(file_path):
# #     try:
# #         with open(file_path, 'r') as file:
# #             lines = file.readlines()

# #             # Define a regular expression pattern to match lines starting with "search"
# #             search_pattern = re.compile(r'^\s*search', re.IGNORECASE)

# #             # Iterate through lines to find and print lines starting with "search"
# #             for line in lines:
# #                 if search_pattern.match(line):
# #                     print(line.strip())

# #     except FileNotFoundError:
# #         print(f"Error: File '{file_path}' not found.")

# # # Example usage
# # file_path = "Sample_Text.conf"  # Replace with the path to your text file
# # find_search_lines(file_path)


# import re

# def find_search_and_rr_lines(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             lines = file.readlines()

#             # Define regular expression patterns
#             search_pattern = re.compile(r'^\s*search', re.IGNORECASE)
#             rr_pattern = re.compile(r'\brule_title', re.IGNORECASE)

#             # Iterate through lines to find and print lines starting with "search" or containing "RR-"
#             for line in lines:
#                 if search_pattern.match(line):
#                     print( line.strip())
#                 elif rr_pattern.search(line):
#                     print(line.strip())

#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")

# # Example usage
# file_path = "Sample_Text.conf"  # Replace with the path to your text file
# find_search_and_rr_lines(file_path)


# # import re

# # def find_search_and_rr_lines(file_path):
# #     try:
# #         with open(file_path, 'r') as file:
# #             lines = file.readlines()

# #             # Define regular expression patterns
# #             search_pattern = re.compile(r'^\s*search', re.IGNORECASE)
# #             rr_pattern = re.compile(r'\bRR-', re.IGNORECASE)
# #             rule_title_pattern = re.compile(r'rule_title', re.IGNORECASE)

# #             # Flag to indicate if "rule_title" is found
# #             rule_title_found = False

# #             # Iterate through lines to find and print lines meeting the conditions
# #             for line in lines:
# #                 if search_pattern.match(line):
# #                     print("Search Line:", line.strip())
# #                     rule_title_found = False
# #                 elif rr_pattern.search(line):
# #                     print("RR Line:", line.strip())
# #                     rule_title_found = False
# #                 elif rule_title_pattern.search(line) and rr_pattern.search(line):
# #                     print("Rule Title and RR Line:", line.strip())
# #                     rule_title_found = True
# #                 elif rule_title_found:
# #                     print("Continuation Line:", line.strip())
# #                     rule_title_found = False

# #     except FileNotFoundError:
# #         print(f"Error: File '{file_path}' not found.")

# # # Example usage
# # file_path = "Sample_Text.conf"  # Replace with the path to your text file
# # find_search_and_rr_lines(file_path)

import re

with open('savedsearches_OC1.txt', 'r') as file:
    for line in file:
        if re.search(r'\brule_alert.*', line):
            print(line)


