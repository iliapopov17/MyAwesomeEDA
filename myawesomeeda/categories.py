def categorize_features(df, unique_threshold=None):
    if unique_threshold is None:
        unique_threshold = int(input("Unique threshold for categorical features: "))

    numerical_features = []
    string_features = []
    categorical_features = []

    for column in df.columns:
        if df[column].nunique() < unique_threshold:
            categorical_features.append(column)
        elif df[column].dtype in ["int64", "float64"]:
            numerical_features.append(column)
        elif df[column].dtype == "object":
            string_features.append(column)

    return numerical_features, string_features, categorical_features


def print_categorical_counts(df, categorical_features):
    print("\033[1m" + "Value Counts and Frequencies:" + "\033[0m")
    for feature in categorical_features:
        counts = df[feature].value_counts()
        total = len(df[feature])

        values_summary = [
            f"{val} = {cnt} ({cnt / total * 100:.2f}%)" for val, cnt in counts.items()
        ]

        print(f"- {feature}: " + ", ".join(values_summary))
