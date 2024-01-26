import re

def parse_text_file_and_save_results(file_path, output_file_path):
    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            file_content = file.read()

            # Define your regular expression pattern
            rules_pattern = r'RR\-.*\]'
            rules = re.findall(rules_pattern, file_content)

            # You can add more regex patterns based on your specific needs
            rule_content = r'.*'
            content = re.findall(rule_content, file_content)

            rule_content_pattern = re.compile(r'{}(.*?){}'.format(rules_pattern, rules_pattern), re.DOTALL)
            rule_contents = [match.group(1).strip() for match in rule_content_pattern.finditer(file_content)]

            # Save results to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write("Rule and associated content found:\n")
                for i, rule in enumerate(rules):
                    if i < len(rule_contents):
                        content = rule_contents[i]
                        output_file.write(f"{i}, Rule: {rule}\n")
                    else:
                        output_file.write(f"Rule: {rule}\n")

            print(f"Results saved to {output_file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'Es_all_search_final.txt' and 'output_results.txt' with the actual paths
parse_text_file_and_save_results('Es_all_search_final.txt', 'new_list4.txt')
