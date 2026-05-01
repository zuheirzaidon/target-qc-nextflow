#!/usr/bin/env python3

import argparse
import pandas as pd


def chunk_region(start: int, end: int, chunk_size: int):
    chunks = []
    current = start
    chunk_index = 1
    while current <= end:
        chunk_end = min(current + chunk_size - 1, end)
        chunks.append((chunk_index, current, chunk_end))
        current = chunk_end + 1
        chunk_index += 1
    return chunks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--chunk-size", required=True, type=int)
    args = parser.parse_args()

    regions = pd.read_csv(args.input)
    rows = []

    for _, row in regions.iterrows():
        for chunk_index, chunk_start, chunk_end in chunk_region(
            int(row["start"]),
            int(row["end"]),
            args.chunk_size
        ):
            rows.append(
                {
                    "region_id": row["region_id"],
                    "gene": row["gene"],
                    "chunk_id": f'{row["region_id"]}_chunk{chunk_index}',
                    "chunk_start": chunk_start,
                    "chunk_end": chunk_end,
                    "chunk_length": chunk_end - chunk_start + 1,
                }
            )

    pd.DataFrame(rows).to_csv(args.output, index=False)


if __name__ == "__main__":
    main()