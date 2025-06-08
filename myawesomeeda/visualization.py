from itertools import cycle
import seaborn as sns
import matplotlib.pyplot as plt
import warnings


COLORS = [
    "#FFF0F0",
    "#F2E4FA",
    "#D6F2FF",
    "#E0F9E9",
    "#FFFAE3",
    "#ECF6CF",
]

color_cycle = cycle(COLORS)


def plot_missing_values(df):
    missing_percentage = df.isnull().mean() * 100
    missing_percentage = missing_percentage[missing_percentage > 0].sort_values(
        ascending=False
    )

    num_features = len(missing_percentage)

    width = max(3, min(0.3 * num_features, 10))
    height = 3
    _ = plt.figure(figsize=(width, height), dpi=200)

    base_font = max(3, 8 - num_features * 0.3)
    label_font = max(2.5, 6 - num_features * 0.25)
    tick_font = max(2.5, 5 - num_features * 0.2)
    annotate_font = max(3, 5 - num_features * 0.2)

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
            fontsize=annotate_font,
            color="black",
            fontweight="bold",
            xytext=(0, 10),
            textcoords="offset points",
        )

    plt.title(
        "Percentage of Missing Values by Variable",
        fontsize=base_font,
        fontweight="bold",
        fontstyle="italic",
    )
    plt.xlabel("Features", fontsize=label_font, fontweight="bold", fontstyle="italic")
    plt.ylabel("Percentage", fontsize=label_font, fontweight="bold", fontstyle="italic")
    plt.xticks(rotation=90, fontsize=tick_font)
    plt.yticks(fontsize=tick_font)

    plt.show()


def plot_correlation_heatmap(df, numerical_features):
    numerical_df = df[numerical_features]
    correlation_matrix = numerical_df.corr()

    num_features = len(numerical_features)

    width = max(4, min(0.6 * num_features, 12))
    plt.figure(figsize=(width, width), dpi=200)

    base_font = max(3, 8 - num_features * 0.3)
    annotate_font = max(3, 5 - num_features * 0.15)
    tick_font = max(2.5, 5 - num_features * 0.2)

    heatmap = sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5,
        annot_kws={"size": annotate_font},
        cbar_kws={"shrink": 0.5},
        square=True,
    )

    heatmap.figure.axes[-1].tick_params(labelsize=annotate_font)

    plt.title(
        "Correlation Heatmap",
        fontsize=base_font,
        fontweight="bold",
        fontstyle="italic",
    )
    plt.xticks(fontsize=tick_font, rotation=45, ha="right")
    plt.yticks(fontsize=tick_font)

    plt.tight_layout()
    plt.show()


def plot_numerical_features(df, numerical_features):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for feature in numerical_features:
            plt.figure(figsize=(7, 3), dpi=200)
            plt.subplot(1, 2, 1)

            sns.boxplot(x=df[feature], color=next(color_cycle))
            plt.title(
                f"Boxplot of {feature}",
                fontsize=6,
                fontweight="bold",
                fontstyle="italic",
            )
            plt.xlabel("Count", fontsize=4, fontweight="bold", fontstyle="italic")
            plt.xticks(fontsize=5)

            plt.subplot(1, 2, 2)
            ax = sns.histplot(df[feature], kde=True, color=next(color_cycle))

            for line in ax.lines:
                line.set_color("gray")

            plt.title(
                f"Histogram of {feature}",
                fontsize=6,
                fontweight="bold",
                fontstyle="italic",
            )
            plt.xlabel(f"{feature}", fontsize=5, fontweight="bold", fontstyle="italic")
            plt.ylabel("Count", fontsize=5, fontweight="bold", fontstyle="italic")
            plt.xticks(fontsize=5)
            plt.yticks(fontsize=5)

            plt.tight_layout()
            plt.show()
