# Localization Key Cleanup Script

This project consists of multiple scripts to identify and remove unused localization keys from a Swift project. The scripts are organized into different modules for better maintainability and clarity.

## Project Structure

- `extract_case_names.py`: Extracts case names and lines from the Swift localization key file.
- `search_project_files.py`: Recursively searches through all files in the project directory to find used keys.
- `find_unused_keys.py`: Combines the functionality of extracting and searching to find unused keys.
- `write_unused_keys.py`: Writes the unused keys and their lines to an output file.
- `delete_unused_keys.py`: Removes unused keys from the Swift localization key file.
- `delete_unused_keys_from_localization.py`: Removes unused keys from the localization `.strings` files.
- `main.py`: The main script to orchestrate the entire process.

## Requirements

- Python 3.x
- Click library (`pip install click`)

## Usage

1. **Ensure you have Python 3.x installed on your machine.**

2. **Install the required Python libraries:**
    ```sh
    pip install click
    ```

3. **Place your Swift localization key file and project directory in the specified paths.**

4. **Run the `main.py` script with appropriate arguments:**
    ```sh
    python main.py --base_language BASE_LANGUAGE_FILE --input PROJECT_DIRECTORY --output OUTPUT_PATH
    ```

### Script Descriptions

#### `extract_case_names.py`
Extracts case names and lines from the specified Swift localization key file.

#### `search_project_files.py`
Recursively searches through all files in the project directory to find which keys are used.

#### `find_unused_keys.py`
Combines the functionality of `extract_case_names` and `search_project_files` to find unused keys.

#### `write_unused_keys.py`
Writes the unused keys and their corresponding lines to an output file.

#### `delete_unused_keys.py`
Removes unused keys from the Swift localization key file.

#### `delete_unused_keys_from_localization.py`
Removes unused keys from the localization `.strings` files.

#### `main.py`
The main script that orchestrates the entire process:
- Finds unused keys
- Writes them to an output file
- Deletes them from the Swift localization key file
- Deletes them from the localization `.strings` files

### Example

To run the script, use the following command:
```sh
python main.py --base_language english.strings --input /path/to/project_directory --output /path/to/output_directory
