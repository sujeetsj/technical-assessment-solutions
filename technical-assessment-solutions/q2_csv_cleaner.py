import csv
import re


def clean_csv_data(input_file, output_file):
    # Regular expression for validating email format
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # Dictionary to store unique entries
    unique_entries = {}

    # Read the input CSV file
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        for row in reader:
            user_id = row['user_id']
            email = row['email']

            # Check if the email is valid
            if email_regex.match(email):
                # If the user_id is new or has a more recent entry, update it
                if user_id not in unique_entries or row['timestamp'] > unique_entries[user_id]['timestamp']:
                    unique_entries[user_id] = row

    # Write the cleaned data to the output CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in unique_entries.values():
            writer.writerow(row)


# Example usage
if __name__ == "__main__":
    input_file = "input_data.csv"
    output_file = "cleaned_data.csv"
    clean_csv_data(input_file, output_file)
    print(f"Cleaned data has been written to {output_file}")