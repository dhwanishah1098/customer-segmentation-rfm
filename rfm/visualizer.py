import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_rfm_distribution(rfm: pd.DataFrame, output_path: str = None):
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    for ax, col, color in zip(axes, ["recency", "frequency", "monetary"], ["#4C72B0", "#55A868", "#C44E52"]):
        sns.histplot(rfm[col], ax=ax, color=color, kde=True)
        ax.set_title(f"{col.capitalize()} Distribution")
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
    return fig


def plot_segment_treemap(segment_df: pd.DataFrame, output_path: str = None):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = plt.cm.Set3.colors
    bars = ax.barh(segment_df["segment"], segment_df["total_revenue"], color=colors[:len(segment_df)])
    ax.set_xlabel("Total Revenue ($)")
    ax.set_title("Revenue by Customer Segment", fontweight="bold")
    for bar, row in zip(bars, segment_df.itertuples()):
        ax.text(bar.get_width() * 0.01, bar.get_y() + bar.get_height() / 2,
                f"{row.customers} customers", va="center", fontsize=9)
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
    return fig


def plot_rfm_heatmap(rfm: pd.DataFrame, output_path: str = None):
    pivot = rfm.pivot_table(index="R_score", columns="F_score", values="monetary", aggfunc="mean")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd", ax=ax)
    ax.set_title("Avg Monetary by R & F Score", fontweight="bold")
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path, dpi=150)
    return fig
