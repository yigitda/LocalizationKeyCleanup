import os
from find_unused_keys import find_unused_keys
from write_unused_keys import write_unused_keys
from delete_unused_keys import delete_unused_keys_from_swift
from delete_unused_keys_from_localization import delete_unused_keys_from_localization

# Paths
swift_file_path = 'insert your path to file incloding keys and cases'
project_directory = 'insert your path to project'
localization_folder_path = 'insert your path to Localization files'
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
output_file_path = os.path.join(desktop_path, 'unused_localization_keys.txt')

# Ensure the Desktop directory exists
os.makedirs(desktop_path, exist_ok=True)

def main():
    case_lines, unused_cases = find_unused_keys(swift_file_path, project_directory)
    write_unused_keys(output_file_path, case_lines, unused_cases)
    delete_unused_keys_from_swift(swift_file_path, unused_cases)
    delete_unused_keys_from_localization(localization_folder_path, unused_cases)
    print(f"Output written to {output_file_path}")
    print("Unused keys have been removed from the Swift file and localization files.")

if __name__ == "__main__":
    main()

