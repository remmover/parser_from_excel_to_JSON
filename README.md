# Excel to JSON Converter

This Python script converts data from Excel files (.xlsx) into JSON format, creating separate JSON files for each sheet in the Excel file. It allows you to customize the columns to parse by modifying specific variables. The script extracts data from the specified columns in the Excel sheets and structures the data into a dictionary format before writing it to JSON files. The script ensures that each key is unique and handles cases where multiple Excel files are present in the specified directory.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [File Structure](#file-structure)
- [Example Excel Files](#example-excel-files)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/remmover/parser_from_excel_to_JSON.git
   ```

2. Navigate to the project directory:

   ```bash
   cd parser_from_excel_to_JSON
   ```

3. Install the required Python libraries using:

   ```bash
   pip install pandas
   ```

## Usage

1. Place your Excel files (with a `.xlsx` extension) in the project directory.

2. Open a terminal and navigate to the project directory.

3. Run the script by executing:

   ```bash
   python parser_from_excel_to_JSON.py
   ```

4. The script will process the Excel files, convert data from each sheet into JSON format, and create corresponding JSON files in the `locales` directory.

## Customization

You can customize the columns that the script will parse by modifying the following variables in the `excel_to_json_converter.py` script:

- `KEY_COLUMN`: The column containing keys for developers.
- `VALUE_COLUMN`: The column containing primary values for translation.
- `EXTRA_VALUE_COLUMN`: The column containing additional values for translation.

Update these variables with the appropriate column names before running the script.

## File Structure

The project directory contains the following files:

- `parser_from_excel_to_JSON.py`: The Python script responsible for converting Excel files to JSON.
- `README.md`: This README file providing information about the project.
- `locales/`: A directory that will be created by the script to store the generated JSON files.

## Example Excel Files

You can find example Excel files in the `examples` directory. These files demonstrate the expected format for the Excel data that the script can process.

## Contributing

Contributions to this project are welcome! If you find any issues or would like to enhance the functionality, please create a pull request or submit an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer:** This project was developed by a single person and serves as a basic Excel to JSON conversion tool. It is recommended to review and test the script on sample data before using it for important tasks. The author is not responsible for any misuse or unintended consequences of using this script.
