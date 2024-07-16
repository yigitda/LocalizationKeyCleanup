import os

def delete_unused_keys_from_localization(localization_folder_path, unused_cases):
    for root, _, files in os.walk(localization_folder_path):
        for file in files:
            if file.endswith('.strings'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as strings_file:
                    strings_content = strings_file.readlines()

                with open(file_path, 'w') as strings_file:
                    for line in strings_content:
                        if not any(f'"{key}"' in line for key in unused_cases):
                            strings_file.write(line)

