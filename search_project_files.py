import os
import re

def search_project_files(directory, case_names):
    unused_cases = set(case_names)
    localized_pattern = re.compile(r'\.localized\(\.(\w+)\)')
    key_pattern = re.compile(r'key\s*=\s*\.(\w+)')
    dot_case_pattern = re.compile(r'\.(\w+)\b')

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', errors='ignore') as project_file:
                try:
                    content = project_file.read()
                except UnicodeDecodeError:
                    continue

                localized_matches = localized_pattern.findall(content)
                key_matches = key_pattern.findall(content)
                dot_case_matches = dot_case_pattern.findall(content)

                for match in localized_matches + key_matches + dot_case_matches:
                    if match in unused_cases:
                        unused_cases.remove(match)
    
    return unused_cases

