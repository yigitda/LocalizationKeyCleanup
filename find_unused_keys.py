from extract_case_names import extract_case_names
from search_project_files import search_project_files

def find_unused_keys(swift_file_path, project_directory):
    case_lines = extract_case_names(swift_file_path)
    case_names = list(case_lines.keys())
    unused_cases = search_project_files(project_directory, case_names)
    return case_lines, unused_cases

