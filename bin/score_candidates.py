#!/usr/bin/env python3

import argparse
import pandas as pd


def score_row(row):
    score = 0.0

    gc_score = max(0, 30 - abs(row["primer_gc"] - 50))
    score += gc_score

    guide_score = row["guide_count"] * 10
    score += guide_score

    length_score = max(0, 20 - abs(row["chunk_length"] - 120) / 2)
    score += length_score

    return round(score, 2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    candidates = pd.read_csv(args.input)
    candidates["design_score"] = candidates.apply(score_row, axis=1)
    candidates.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()