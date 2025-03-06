import pandas as pd

def split_excel_by_column(input_file, column_name, output_file="output.xlsx"):
    # Load the Excel file
    df = pd.read_excel(input_file)

    # Create a Pandas Excel writer
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        # Iterate through unique values in the column
        for value in df[column_name].unique():
            # Filter data based on the column value
            filtered_df = df[df[column_name] == value]
            
            # Write to a new sheet named after the column value
            filtered_df.to_excel(writer, sheet_name=str(value), index=False)

    print(f"File saved as {output_file}")

# Example usage
# split_excel_by_column("input.xlsx", "Category")  # Replace "Category" with the actual column name