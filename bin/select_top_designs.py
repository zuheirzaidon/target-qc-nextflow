#!/usr/bin/env python3

import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    scored = pd.read_csv(args.input)
    top = (
        scored.sort_values(["chunk_id", "design_score"], ascending=[True, False])
        .groupby("chunk_id", as_index=False)
        .head(1)
        .reset_index(drop=True)
    )
    top.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()