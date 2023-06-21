# Excel to JSON Converter

This is a Python script that converts Excel files (.xlsx) into JSON files. It reads each sheet in the Excel file, extracts specific columns, and converts the data into a JSON format. The resulting JSON files can be used for localization or any other purpose requiring JSON data.

## Prerequisites

To run this script, you need to have the following installed:

- Python 3.x
- pandas library (`pip install pandas`)

## Usage

1. Place the Excel files you want to convert into the same directory as the script.
2. Open a terminal or command prompt and navigate to the directory containing the script.
3. Run the following command:

```shell
python excel_to_json_converter.py
```

The script will process all the Excel files in the directory and generate corresponding JSON files in a new directory called "locales".

## Customization

If you need to modify the script to suit your specific requirements, you can edit the following parts:

- **Excel Columns**: The script currently assumes that the relevant columns in the Excel file are named "Keys for developers" and the filename (without the extension). If your Excel files have different column names, you can update them in the `usecols` parameter of the `pd.read_excel()` function.

- **Output Directory**: By default, the script creates a "locales" directory to store the generated JSON files. If you want to change the output directory, you can modify the `json_file` variable in the script.

## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use it according to your needs.

## Acknowledgements

- This script utilizes the [pandas](https://pandas.pydata.org/) library for reading Excel files and data manipulation.
- Developed by [Your Name]

## Troubleshooting

If you encounter any issues or have questions, please [open an issue](https://github.com/remmover/Parser.git) on the repository.
