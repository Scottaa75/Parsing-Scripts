# import configparser

# config = configparser.ConfigParser()

# config.read('Sample_Text.conf')

# for section in config.sections():
#     print(f'Section: {section}')
#     for key, value in config.items(section):
#         print(f'{key} = {value}')


import configparser

def read_savedsearches_config(file_path):
    config = configparser.ConfigParser()
    config.optionxform = str  # Preserve case sensitivity
    config.read(file_path)

    for savedsearch in config.sections():
        print(f"[{savedsearch}]")
        for key, value in config.items(savedsearch):
            print(f"{key} = {value}")
        print()  # Add an empty line between saved searches

# Example usage
file_path = "savedsearches.conf"  # Replace with the path to your savedsearches.conf file
read_savedsearches_config(file_path)
