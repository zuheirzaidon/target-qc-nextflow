#!/usr/bin/env python3

import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--designs", required=True)
    parser.add_argument("--qc", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    designs = pd.read_csv(args.designs)
    qc = pd.read_csv(args.qc)

    merged = designs.merge(qc, on=["candidate_id", "gene"], how="left")

    summary = (
        merged.groupby("gene", as_index=False)
        .agg(
            selected_designs=("candidate_id", "count"),
            mean_design_score=("design_score", "mean"),
            mean_total_reads=("total_reads", "mean"),
            mean_mapped_reads_pct=("mapped_reads_pct", "mean"),
            mean_on_target_pct=("on_target_pct", "mean"),
            mean_uniformity_pct=("uniformity_pct", "mean"),
            qc_pass_count=("qc_status", lambda s: (s == "PASS").sum()),
            qc_review_count=("qc_status", lambda s: (s == "REVIEW").sum()),
        )
    )

    numeric_cols = [
        "mean_design_score",
        "mean_total_reads",
        "mean_mapped_reads_pct",
        "mean_on_target_pct",
        "mean_uniformity_pct",
    ]
    summary[numeric_cols] = summary[numeric_cols].round(2)

    summary.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()