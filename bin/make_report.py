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

    total_designs = len(designs)
    total_pass = int((qc["qc_status"] == "PASS").sum())
    total_review = int((qc["qc_status"] == "REVIEW").sum())
    mean_score = round(designs["design_score"].mean(), 2)
    mean_on_target = round(qc["on_target_pct"].mean(), 2)

    lines = [
        "Target QC Nextflow Report",
        "=========================",
        "",
        f"Selected designs: {total_designs}",
        f"Mean design score: {mean_score}",
        f"Mean on-target %: {mean_on_target}",
        f"QC PASS count: {total_pass}",
        f"QC REVIEW count: {total_review}",
        "",
        "Designs by gene:",
    ]

    for gene, count in designs.groupby("gene").size().items():
        lines.append(f"- {gene}: {count}")

    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))


if __name__ == "__main__":
    main()