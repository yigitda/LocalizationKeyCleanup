def write_unused_keys(output_file_path, case_lines, unused_cases):
    with open(output_file_path, 'w') as output_file:
        if unused_cases:
            output_file.write("Unused localization keys and their lines:\n")
            for case in unused_cases:
                output_file.write(f"{case_lines[case]}\n")
        else:
            output_file.write("All localization keys are used in the project.\n")
