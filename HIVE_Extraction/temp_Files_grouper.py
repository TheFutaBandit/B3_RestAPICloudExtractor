import pandas as pd
import csv

def aggregate_bug_ids(input_csv, output_csv):
    """Aggregate Bug IDs for each unique file and export the results to a new CSV."""
    # Read the input CSV file
    df = pd.read_csv(input_csv)

    # Group by the 'File' column and aggregate Bug IDs into a comma-separated string
    df_aggregated = df.groupby('File')['Bug_ID'].apply(lambda x: ','.join(x)).reset_index()

    # Write the results to the output CSV file
    df_aggregated.to_csv(output_csv, index=False, quoting=csv.QUOTE_NONNUMERIC)

def main():
    input_csv = 'dataset/HIVE_ExistingFiles_JavaFilter.csv'  # Input CSV file with possibly repeated files
    output_csv = 'dataset/HIVE_AggregatedFiles_JavaFilter.csv'  # Output CSV file with aggregated Bug IDs
    aggregate_bug_ids(input_csv, output_csv)
    print(f"Processed CSV file and exported aggregated results to {output_csv}")

if __name__ == "__main__":
    main()
