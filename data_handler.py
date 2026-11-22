import pandas as pd


# Load medicine dataset
def load_medicine_data():
    df = pd.read_csv("medicine_data.csv")

    # Remove unnecessary spaces from column names
    df.columns = df.columns.str.strip()

    # Clean medicine names
    df["Medicine Name"] = df["Medicine Name"].astype(str).str.strip()

    return df


# Search medicine by name
def search_medicine(medicine_name, df):

    medicine_name = medicine_name.strip().lower()

    if not medicine_name:
        return None, []

    # First: Exact match
    exact_match = df[df["Medicine Name"].str.lower() == medicine_name]

    if not exact_match.empty:
        return exact_match.iloc[0].to_dict(), []

    # Second: Partial match
    partial_matches = df[
        df["Medicine Name"]
        .str.lower()
        .str.contains(medicine_name, regex=False, na=False)
    ]

    if partial_matches.empty:
        return None, []

    # Return all partial matches for user selection
    return None, partial_matches["Medicine Name"].tolist()


# Run directly to test the search engine
if __name__ == "__main__":

    df = load_medicine_data()

    print("Medicine Lookup Engine")
    print("Total medicines:", len(df))

    while True:

        medicine = input("\nEnter medicine name (or exit): ")

        if medicine.lower() == "exit":
            break

        result, suggestions = search_medicine(medicine, df)

        if result is not None:

            print("\nMedicine Found!")
            print("Name:", result["Medicine Name"])
            print("Composition:", result["Composition"])
            print("Uses:", result["Uses"])
            print("Side Effects:", result["Side_effects"])
            print("Manufacturer:", result["Manufacturer"])

        elif suggestions:

            print("\nMultiple or partial matches found:")

            for item in suggestions[:10]:
                print("-", item)

        else:

            print("\nMedicine not found in dataset.")
