import pandas as pd

def process_data_from_csv(cols, power):
    data = pd.read_csv('alloy-confp-train-data_v2.csv')

    # Check if selected columns contain non-numeric values
    non_numeric_cols = [col for col in cols if not pd.api.types.is_numeric_dtype(data[col])]

    if non_numeric_cols:
        print(f"Error: Columns {non_numeric_cols} contain non-numeric values.")
        return None

    selected_data = data[cols]

    powered_data = selected_data ** power

    return powered_data

cols = ['C.al', 'C.cr']
power = [2, 3]

result = process_data_from_csv(cols, power)

if result is not None:
    print(result)
