import re

def find_search_and_rr_lines(file_path, output_file):

    with open(file_path, 'r') as file, open(output_file, 'w') as output:
        lines = file.readlines()

        # Define regular expression patterns
        search_pattern = re.compile(r'^\s*search', re.IGNORECASE)
        rr_pattern = re.compile(r'\bRR-', re.IGNORECASE)
        rule_alerts_pattern = re.compile(r'\brule_alerts', re.IGNORECASE)

        # Iterate through lines to find and write lines meeting the conditions
        for line in lines:
            if rule_alerts_pattern.search(line) and rr_pattern.search(line):
                output.write(line)
            
            elif search_pattern.match(line) or rr_pattern.search(line):
                output.write(line + '\n')

    
file_path = "Es_all_search_final.txt"  
output_file = "new_results.txt"  
find_search_and_rr_lines(file_path, output_file)
