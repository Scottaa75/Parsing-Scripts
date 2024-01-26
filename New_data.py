import re

def parse_text(file_path, output_file):
    
    with open(file_path, 'r') as file:
        
        file_content = file.read()
                
        rule_pattern = r'RR\-.*\]'
        rule_content_pattern = re.compile(r'{}(.*?){}'.format(rule_pattern, rule_pattern), re.DOTALL)

        matches = rule_content_pattern.finditer(file_content)

        with open(output_file, 'w') as output:
            

            for match in matches:
                
                rules = re.findall(rule_pattern, match.group(0))
                content = match.group(1).strip()

                for count, rule in enumerate(rules):
                    output.write(f"\n{count} [{rule} \n{content} \n")
                    
                
 


parse_text('savedsearches_OC1.txt', 'output2.txt')
