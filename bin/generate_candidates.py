#!/usr/bin/env python3

import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--num-candidates", required=True, type=int)
    args = parser.parse_args()

    chunks = pd.read_csv(args.input)
    rows = []

    for _, row in chunks.iterrows():
        for design_rank in range(1, args.num_candidates + 1):
            rows.append(
                {
                    "region_id": row["region_id"],
                    "gene": row["gene"],
                    "chunk_id": row["chunk_id"],
                    "candidate_id": f'{row["chunk_id"]}_cand{design_rank}',
                    "primer_gc": 38 + design_rank * 4,
                    "guide_count": design_rank,
                    "chunk_length": row["chunk_length"],
                }
            )

    pd.DataFrame(rows).to_csv(args.output, index=False)


if __name__ == "__main__":
    main()