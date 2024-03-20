import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, HTML

COLORS = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]


def display_welcome_gif():
    html_code = """
    <img src="imgs/welcome.gif" width="200" height="200">
    """
    display(HTML(html_code))


def display_hruler():
    print()
    print(" ".join([f"{color}\033[1m=====\033[0m" for color in COLORS]))
    print(" ".join([f"{color}\033[1m=====\033[0m" for color in reversed(COLORS)]))


def run_eda(df):

    print("\033[1;95m" + "Welcome to the Awesome EDA Module!" + "\033[0m")

    display_welcome_gif()

    print("\033[1m" + "\nNumber of observations (rows):\n" + "\033[0m" f"{df.shape[0]}")
    print("\033[1m" + "Number of parameters (columns):\n" + "\033[0m" f"{df.shape[1]}")

    display_hruler()

    data_types = df.dtypes
    print("\033[1m" + "\nData types of each column:" + "\033[0m")

    for line in data_types.to_string().splitlines()[0:]:
        print(line)

    display_hruler()

    def categorize_features(
        df, unique_threshold=int(input("Unique threshold for categorical features:"))
    ):
        numerical_features = []
        string_features = []
        categorical_features = []

        for column in df.columns:
            if df[column].nunique() < unique_threshold:  # it can be regulated manually
                categorical_features.append(column)
            elif df[column].dtype in ["int64", "float64"]:
                numerical_features.append(column)
            elif df[column].dtype == "object":
                string_features.append(column)

        return numerical_features, string_features, categorical_features

    numerical_features, string_features, categorical_features = categorize_features(df)

    print("\033[1m" + "\nNumerical features:\n" + "\033[0m" f"{numerical_features}")
    print("\033[1m" + "\nString features:\n" + "\033[0m" f"{string_features}")
    print("\033[1m" + "\nCategorical features:\n" + "\033[0m" f"{categorical_features}")

    display_hruler()

    def print_categorical_counts(df, categorical_features):
        for feature in categorical_features:
            print(
                "\033[1m" + "\nCounts and frequencies for " + f"{feature}:" + "\033[0m"
            )
            counts = df[feature].value_counts()
            total_counts = len(df[feature])

            results = [
                {
                    "Value": value,
                    "Counts": count,
                    "Frequencies": count / total_counts * 100,
                }
                for value, count in counts.items()
            ]

            for row in results:
                print(
                    f"{row['Value']}: Counts={row['Counts']}, Frequencies={row['Frequencies']:.2f}%"
                )

    print_categorical_counts(df, categorical_features)

    display_hruler()

    numerical_summary = df[numerical_features].describe()
    print(
        "\033[1m" + "\nSummary statistics for numerical features:\n" + "\033[0m"
        f"{numerical_summary}"
    )

    def print_outliers_count(df, numerical_features):
        print("\033[1m" + "\nOutliers count for numerical features:" + "\033[0m")
        for feature in numerical_features:

            q1 = df[feature].quantile(0.25)
            q3 = df[feature].quantile(0.75)
            iqr = q3 - q1

            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            outliers_count = df[
                (df[feature] < lower_bound) | (df[feature] > upper_bound)
            ].shape[0]

            print(f"Outliers count for {feature}: {outliers_count}")

    print_outliers_count(df, numerical_features)

    display_hruler()

    total_missing = df.isnull().sum().sum()
    rows_with_missing = df[df.isnull().any(axis=1)].shape[0]
    columns_with_missing = df.columns[df.isnull().any()].tolist()

    print("\033[1m" + "\nTotal missing values:\n" + "\033[0m" f"{total_missing}")
    print("\033[1m" + "Rows with missing values:\n" + "\033[0m" f"{rows_with_missing}")
    print(
        "\033[1m" + "Columns with missing values:\n" + "\033[0m"
        f"{columns_with_missing}"
    )

    duplicate_rows = df[df.duplicated()]
    num_duplicate_rows = duplicate_rows.shape[0]
    print(
        "\033[1m" + "\nNumber of duplicate rows:\n" + "\033[0m" f"{num_duplicate_rows}"
    )

    display_hruler()

    def plot_missing_values(df):
        plt.figure(figsize=(12, 6))

        missing_percentage = df.isnull().mean() * 100
        missing_percentage = missing_percentage[missing_percentage > 0].sort_values(
            ascending=False
        )

        ax = sns.barplot(
            x=missing_percentage.index,
            y=missing_percentage.values,
            hue=missing_percentage.index,
            palette="viridis",
            legend=False,
        )
        ax.set(ylim=(0, 100))

        for p in ax.patches:
            ax.annotate(
                f"{p.get_height():.1f}%",
                (p.get_x() + p.get_width() / 2.0, p.get_height()),
                ha="center",
                va="center",
                fontsize=10,
                color="black",
                fontweight="bold",
                xytext=(0, 10),
                textcoords="offset points",
            )

        plt.title(
            "Percentage of Missing Values by Variable",
            fontsize=16,
            fontweight="bold",
            fontstyle="italic",
        )
        plt.xlabel("Features", fontsize=12, fontweight="bold", fontstyle="italic")
        plt.ylabel("Percentage", fontsize=12, fontweight="bold", fontstyle="italic")
        plt.xticks(rotation=90)

        plt.show()

    plot_missing_values(df)

    display_hruler()

    def plot_correlation_heatmap(df, numerical_features):
        numerical_df = df[numerical_features]

        correlation_matrix = numerical_df.corr()

        plt.figure(figsize=(10, 8))
        sns.heatmap(
            correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5
        )

        plt.title(
            "Correlation heat map", fontsize=16, fontweight="bold", fontstyle="italic"
        )

        plt.show()

    plot_correlation_heatmap(df, numerical_features)

    display_hruler()

    def plot_numerical_histograms(df, numerical_features):
        for feature in numerical_features:
            plt.figure(figsize=(10.2, 6))
            plt.subplot(2, 1, 1)

            sns.boxplot(x=df[feature], color="skyblue")
            plt.title(
                f"Boxplot of {feature}",
                fontsize=12,
                fontweight="bold",
                fontstyle="italic",
            )
            plt.xlabel("Count", fontsize=8, fontweight="bold", fontstyle="italic")

            plt.subplot(2, 1, 2)
            sns.histplot(df[feature], kde=True, color="skyblue")
            plt.title(
                f"Histogram of {feature}",
                fontsize=8,
                fontweight="bold",
                fontstyle="italic",
            )
            plt.xlabel(f"{feature}", fontsize=8, fontweight="bold", fontstyle="italic")
            plt.ylabel("Count", fontsize=8, fontweight="bold", fontstyle="italic")

            plt.tight_layout()
            plt.show()

    plot_numerical_histograms(df, numerical_features)

    display_hruler()
