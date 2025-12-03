import matplotlib.pyplot as plt

def plot_cpi_trend(df, date_col, value_col):
    """
    Creates a simple line plot for CPI trend.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(df[date_col], df[value_col])
    plt.title("Kenya CPI Trend")
    plt.xlabel(date_col)
    plt.ylabel(value_col)
    plt.grid(True)
    plt.show()
