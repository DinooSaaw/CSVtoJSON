# CSV to JSON Converter

This is a simple Python script that reads in a CSV file and converts it to a JSON file. The script uses the `csv` and `json` modules from the Python Standard Library.

## Usage

To use the script, run the following command in your terminal:

    python csv_to_json.py

The script will prompt you to enter the name of the input CSV file and the name of the output JSON file. You can enter the file names with or without file extensions.

For example:

    Enter the name of the input CSV file (or 'q' to quit): input_data.csv
    Enter the name of the output JSON file: output_data.json

Once you have entered the input and output file names, the script will read in the CSV data, convert it to a JSON object, and write it to the output file. If the conversion is successful, the script will print a success message and prompt you to enter new file names or quit.
## Requirements

This script requires Python 3.6 or higher. The `csv` and `json` modules are included in the Python Standard Library, so no additional packages need to be installed.
