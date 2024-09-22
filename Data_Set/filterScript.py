import csv

def filter_public_classes(input_csv, output_csv):
    with open(input_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames  # Retain the original column names
        
        public_classes = []

        # Filter rows where the 'Kind' column contains 'Public Class'
        for row in reader:
            if row['Kind'] == 'Public Class':  # Adjusted to match 'Public Class'
                public_classes.append(row)

    # Write the filtered rows to a new CSV file, preserving all columns
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        writer.writerows(public_classes)  # Write the filtered rows

if __name__ == '__main__':
    input_csv_file = '/Users/gaurav/hive/llap-ext-client/src/java/org/apache/hadoop/hive/hivemidsem.csv'  # Replace with the actual path to your input CSV file
    output_csv_file = '/Users/gaurav/hive/llap-ext-client/src/java/org/apache/hadoop/hive/hivemidsemfinal.csv'  # Replace with the desired path to save the output CSV
    filter_public_classes(input_csv_file, output_csv_file)

    print(f"Filtered CSV saved as {output_csv_file}")