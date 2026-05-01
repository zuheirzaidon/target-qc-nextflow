#!/usr/bin/env python3

import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    designs = pd.read_csv(args.input)
    rows = []

    for i, row in designs.iterrows():
        rows.append(
            {
                "candidate_id": row["candidate_id"],
                "gene": row["gene"],
                "total_reads": 100000 + i * 5000,
                "mapped_reads_pct": round(92.0 - i * 0.8, 2),
                "on_target_pct": round(85.0 - i * 0.6, 2),
                "uniformity_pct": round(88.0 - i * 0.5, 2),
                "qc_status": "PASS" if i % 4 != 3 else "REVIEW",
            }
        )

    pd.DataFrame(rows).to_csv(args.output, index=False)


if __name__ == "__main__":
    main()