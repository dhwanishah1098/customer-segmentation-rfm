import argparse
import pandas as pd
from rfm.calculator import calculate_rfm, score_rfm
from rfm.segmentation import assign_segments, segment_summary
from rfm.visualizer import plot_rfm_distribution, plot_segment_treemap, plot_rfm_heatmap
import os


def run(input_path: str):
    df = pd.read_csv(input_path, parse_dates=["order_date"])
    df["revenue"] = df["units_sold"] * df["unit_price"]

    rfm = calculate_rfm(df)
    rfm = score_rfm(rfm)
    rfm = assign_segments(rfm)

    os.makedirs("output", exist_ok=True)
    summary = segment_summary(rfm)
    print(summary.to_string(index=False))

    rfm.to_csv("output/rfm_results.csv", index=False)
    summary.to_csv("output/segment_summary.csv", index=False)

    plot_rfm_distribution(rfm, "output/rfm_distribution.png")
    plot_segment_treemap(summary, "output/segment_treemap.png")
    plot_rfm_heatmap(rfm, "output/rfm_heatmap.png")
    print("Output saved to /output/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()
    run(args.input)
