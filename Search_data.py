import re

def parse_text_file(file_path, output_file):
    try:
        with open(file_path, 'r') as file:
            # Read the content of the file
            file_content = file.read()
            
            # Define your regular expression patterns
            rule_pattern = r'RR\-.*\]'
            rule_content_pattern = re.compile(r'{}(.*?){}'.format(rule_pattern, rule_pattern), re.DOTALL)

            matches = rule_content_pattern.finditer(file_content)

            with open(output_file, 'w') as output:
                counter = 0

                for match in matches:
                    counter += 1
                    rules = re.findall(rule_pattern, match.group(0))
                    content = match.group(1).strip()

                    output.write(f"Number of matches: {counter}\n")
                    for i, rule in enumerate(rules):
                        output.write(f"[{rule}]\n{content}\n")
                    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_file.txt' with the path to your text file
parse_text_file('savedsearches_OC1.txt', 'output.txt')
