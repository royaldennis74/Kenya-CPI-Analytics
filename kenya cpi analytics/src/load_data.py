import pandas as pd

def clean_cpi_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Create Date column
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
    df = df.sort_values('Date')

    # Drop duplicates
    df = df.drop_duplicates()

    # Save cleaned data
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    clean_cpi_data("../data/raw/kenya_cpi_sample.csv", "../data/cleaned/cpi_cleaned.csv")
