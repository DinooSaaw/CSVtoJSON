import csv
import json

while True:
    # Get input and output filenames from user
    input_file = input("Enter the name of the input CSV file (or 'q' to quit): ")
    if input_file.lower() == 'q':
        break
    output_file = input("Enter the name of the output JSON file: ")

    try:
        with open(input_file, newline='') as csvfile:
            # Create a CSV reader object
            reader = csv.DictReader(csvfile)

            # Get the header row
            header_row = reader.fieldnames

            # Create an empty list to store the data rows
            data_rows = []

            # Loop through the rows in the CSV file
            for row in reader:
                # Add each row to the list of data rows
                data_rows.append(row)

        # Create a dictionary to store the header and data rows
        data_dict = {'header': header_row, 'data': data_rows}

        # Write the dictionary to a JSON file
        with open(output_file, 'w') as jsonfile:
            json.dump(data_dict, jsonfile, indent=4)
            print(f"Successfully completed conversion from {input_file} to {output_file}.\n")

    except FileNotFoundError:
        print(f"ERROR: Could not find file {input_file}. Please try again.\n")
    except csv.Error:
        print(f"ERROR: Could not read CSV data from file {input_file}. Please try again.\n")
    except json.JSONDecodeError:
        print(f"ERROR: Could not write JSON data to file {output_file}. Please try again.\n")
