import re

def parse_text_file(file_path, output_file_path):

    with open(file_path, 'r') as file:
        
        file_content = file.read()

        # Define your regular expression pattern for RR rules
        rules_pattern = r'RR\-[^\]]+\]'
        rule_content_pattern = re.compile(r'{}(.*?){}'.format(rules_pattern, rules_pattern), re.DOTALL)

        # Find all occurrences of RR rules and associated content
        matches = rule_content_pattern.finditer(file_content)

        # Use a set to store unique RR rules
        unique_rules = set()

        # Open the output file for writing
        with open(output_file_path, 'w') as output_file:
            # Loop through each set of RR rule and content
            for count, match in enumerate(matches):
                rule = match.group(0)
                content = match.group(1).strip()

                # Check if the RR rule is unique, and process only if it's not a duplicate
                if rule not in unique_rules:
                    unique_rules.add(rule)

                    # Write the unique RR rule and content to the output file
                    output_file.write(f"\n{count} [{rule},\n")

            

   

# Replace 'new_searches.txt' with the path to your text file
# Replace 'output_results.txt' with the desired output file path
parse_text_file('Es_all_search_final.txt', 'list.txt')
