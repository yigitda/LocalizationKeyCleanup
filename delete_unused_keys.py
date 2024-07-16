def delete_unused_keys_from_swift(swift_file_path, unused_cases):
    with open(swift_file_path, 'r') as file:
        swift_content = file.readlines()

    with open(swift_file_path, 'w') as file:
        for line in swift_content:
            if not any(f'case {key} ' in line for key in unused_cases):
                file.write(line)

