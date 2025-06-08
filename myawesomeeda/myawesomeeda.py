from pathlib import Path
import shutil
from .customization import display_welcome_gif, display_hruler
from .categories import categorize_features, print_categorical_counts
from .visualization import (
    plot_missing_values,
    plot_correlation_heatmap,
    plot_numerical_features,
)


def run_eda(df):

    print("\033[1;95m" + "Welcome to the Awesome EDA Module!" + "\033[0m")

    display_welcome_gif()

    print("\033[1m" + "\nNumber of observations (rows):\n" + "\033[0m" f"{df.shape[0]}")
    print("\033[1m" + "Number of parameters (columns):\n" + "\033[0m" f"{df.shape[1]}")

    # ===== ===== ===== ===== ===== =====
    # ===== ===== ===== ===== ===== =====

    display_hruler()

    data_types = df.dtypes
    print("\033[1mColumn Data Types:\033[0m")

    type_to_columns = {}

    for col, dtype in data_types.items():
        dtype_str = str(dtype)
        type_to_columns.setdefault(dtype_str, []).append(col)

    for dtype, columns in type_to_columns.items():
        print(f"- {dtype}: {', '.join(columns)}")

    # ===== ===== ===== ===== ===== =====
    # ===== ===== ===== ===== ===== =====

    display_hruler()

    numerical_features, string_features, categorical_features = categorize_features(df)

    print("\033[1mFeature Categories:\033[0m")
    print(f"- Numerical: {numerical_features}")
    print(f"- Strings: {string_features}")
    print(f"- Categoricals: {categorical_features}")

    # ===== ===== ===== ===== ===== =====
    # ===== ===== ===== ===== ===== =====

    display_hruler()

    print_categorical_counts(df, categorical_features)

    # ===== ===== ===== ===== ===== =====
    # ===== ===== ===== ===== ===== =====

    display_hruler()

    numerical_summary = df[numerical_features].describe()
    print(
        "\033[1m" + "\nSummary statistics for numerical features:\n" + "\033[0m"
        f"{numerical_summary}"
    )

    def print_outliers_count(df, numerical_features):
        print("\033[1m" + "\nOutliers count for numerical features:" + "\033[0m")

        outliers_summary = []

        for feature in numerical_features:
            q1 = df[feature].quantile(0.25)
            q3 = df[feature].quantile(0.75)
            iqr = q3 - q1

            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            outliers_count = df[
                (df[feature] < lower_bound) | (df[feature] > upper_bound)
            ].shape[0]

            outliers_summary.append(f"{feature}: {outliers_count}")

        print(" | ".join(outliers_summary))

    print_outliers_count(df, numerical_features)

    # ===== ===== ===== ===== ===== =====
    # ===== ===== ===== ===== ===== =====

    display_hruler()

    total_missing = df.isnull().sum().sum()
    rows_with_missing = df[df.isnull().any(axis=1)].shape[0]
    columns_with_missing = df.columns[df.isnull().any()].tolist()

    print("\033[1mMissing Data Summary:\033[0m")
    print(f"- Total missing values: {total_missing}")
    print(f"- Rows with missing values: {rows_with_missing}")
    print(f"- Columns with missing values: {columns_with_missing}")

    duplicate_rows = df[df.duplicated()]
    num_duplicate_rows = duplicate_rows.shape[0]
    print(
        "\033[1m" + "\nNumber of duplicate rows:\n" + "\033[0m" f"{num_duplicate_rows}"
    )

    # ===== ===== ===== ===== ===== =====
    # ===== ===== ===== ===== ===== =====

    display_hruler()

    plot_missing_values(df)

    # ===== ===== ===== ===== ===== =====
    # ===== ===== ===== ===== ===== =====

    display_hruler()

    plot_correlation_heatmap(df, numerical_features)

    # ===== ===== ===== ===== ===== =====
    # ===== ===== ===== ===== ===== =====

    display_hruler()

    plot_numerical_features(df, numerical_features)

    # ===== ===== ===== ===== ===== =====
    # ===== ===== ===== ===== ===== =====

    display_hruler()

    current_dir = Path(__file__).resolve().parent
    pycache_dir = current_dir / "__pycache__"
    if pycache_dir.exists() and pycache_dir.is_dir():
        shutil.rmtree(pycache_dir)
