import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# File path
csv_file = 'customer_transactions.csv'

try:
    # Load the dataset
    df = pd.read_csv(csv_file)

    # Ensure the required column exists
    if 'transaction_amount' not in df.columns:
        raise KeyError("The column 'transaction_amount' is missing from the dataset.")

    # Handle missing values: fill with mean for 'transaction_amount'
    df['transaction_amount'].fillna(df['transaction_amount'].mean(), inplace=True)

    # Remove duplicates
    df = df.drop_duplicates()

    # Display basic summary statistics
    print("Summary Statistics:")
    print(df.describe())

    # Visualizations
    # Histogram for 'transaction_amount'
    plt.figure(figsize=(8, 6))
    sns.histplot(df['transaction_amount'], kde=True)
    plt.title('Transaction Amount Distribution')
    plt.xlabel('Transaction Amount')
    plt.ylabel('Frequency')
    plt.show()

    # Boxplot for 'transaction_amount'
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df['transaction_amount'])
    plt.title('Boxplot of Transaction Amount')
    plt.xlabel('Transaction Amount')
    plt.show()

    # Correlation heatmap for numerical features
    if df.select_dtypes(include='number').shape[1] > 1:  # Ensure at least 2 numerical columns for correlation
        plt.figure(figsize=(8, 6))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
        plt.title('Correlation Heatmap')
        plt.show()
    else:
        print("Not enough numerical columns for a correlation heatmap.")

except FileNotFoundError:
    print(f"Error: File '{csv_file}' not found. Ensure it exists in the working directory.")
except KeyError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
