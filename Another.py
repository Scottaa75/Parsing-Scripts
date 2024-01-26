import re

def parse_text(file_path, output_file):

    with open(file_path, 'r') as file:
        file_content = file.read()
        rule_pattern = r'RR-[^-]+ - Rule\]'
        rule_content_pattern = re.compile(r'{}(.*?){}'.format(rule_pattern, rule_pattern), re.DOTALL)
        matches = rule_content_pattern.finditer(file_content)

        with open(output_file, 'w') as output:
            for match in matches:
                rules = re.findall(r'RR-[^-]+ - Rule\]', match.group(1))
                

                for count, rule in enumerate(rules, start=1):
                    output.write(f"\n{count} [{rule}]\n")

parse_text('Es_all_search_final.txt', 'New_list2.txt')
