import re

def parse_text_file(file_path):
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

            # Print rule and contents
            print("Rule and associated content found:")
            for i, rule in enumerate(rules):
                if i < len(rule_contents):
                    content = rule_contents[i]
                    print(f"{i}, Rule: {rule}")
                else:
                    print(f" {rule}, ")



    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

parse_text_file('Es_all_search_final.txt')
