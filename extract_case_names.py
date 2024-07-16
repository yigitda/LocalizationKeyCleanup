import re

def extract_case_names(swift_file_path):
    case_pattern = re.compile(r'case\s+(\w+)\s*=\s*"[^"]+"')
    case_lines = {}

    with open(swift_file_path, 'r') as swift_file:
        for line in swift_file:
            match = case_pattern.search(line)
            if match:
                case_name = match.group(1)
                case_lines[case_name] = line.strip()

    return case_lines
