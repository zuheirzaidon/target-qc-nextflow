#!/usr/bin/env python3

import argparse
from pathlib import Path
import pandas as pd


def dataframe_to_html_table(df: pd.DataFrame, index: bool = False) -> str:
    return df.to_html(index=index, classes="dataframe", border=0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--designs", required=True)
    parser.add_argument("--qc", required=True)
    parser.add_argument("--gene-summary", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    designs = pd.read_csv(args.designs)
    qc = pd.read_csv(args.qc)
    gene_summary = pd.read_csv(args.gene_summary)

    total_designs = len(designs)
    total_pass = int((qc["qc_status"] == "PASS").sum())
    total_review = int((qc["qc_status"] == "REVIEW").sum())
    mean_score = round(designs["design_score"].mean(), 2)
    mean_on_target = round(qc["on_target_pct"].mean(), 2)
    mean_mapped = round(qc["mapped_reads_pct"].mean(), 2)

    designs_preview = designs.head(10).copy()
    qc_preview = qc.head(10).copy()

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Target QC Nextflow Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 40px;
      color: #222;
      line-height: 1.5;
    }}
    h1, h2 {{
      color: #111;
    }}
    .summary-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-bottom: 32px;
    }}
    .card {{
      border: 1px solid #ddd;
      border-radius: 10px;
      padding: 16px;
      background: #fafafa;
    }}
    .metric {{
      font-size: 1.8rem;
      font-weight: bold;
      margin-top: 8px;
    }}
    table.dataframe {{
      border-collapse: collapse;
      width: 100%;
      margin-bottom: 32px;
      font-size: 0.95rem;
    }}
    table.dataframe th,
    table.dataframe td {{
      border: 1px solid #ddd;
      padding: 8px 10px;
      text-align: left;
    }}
    table.dataframe th {{
      background: #f3f3f3;
    }}
    .section {{
      margin-top: 32px;
    }}
    .muted {{
      color: #666;
      font-size: 0.95rem;
    }}
  </style>
</head>
<body>
  <h1>Target QC Nextflow Report</h1>
  <p class="muted">
    Summary report for chunking, candidate generation, scoring, selection, QC simulation, and gene-level aggregation.
  </p>

  <div class="summary-grid">
    <div class="card">
      <div>Total selected designs</div>
      <div class="metric">{total_designs}</div>
    </div>
    <div class="card">
      <div>Mean design score</div>
      <div class="metric">{mean_score}</div>
    </div>
    <div class="card">
      <div>Mean mapped reads %</div>
      <div class="metric">{mean_mapped}</div>
    </div>
    <div class="card">
      <div>Mean on-target %</div>
      <div class="metric">{mean_on_target}</div>
    </div>
    <div class="card">
      <div>QC PASS count</div>
      <div class="metric">{total_pass}</div>
    </div>
    <div class="card">
      <div>QC REVIEW count</div>
      <div class="metric">{total_review}</div>
    </div>
  </div>

  <div class="section">
    <h2>Gene summary</h2>
    {dataframe_to_html_table(gene_summary)}
  </div>

  <div class="section">
    <h2>Selected designs preview</h2>
    {dataframe_to_html_table(designs_preview)}
  </div>

  <div class="section">
    <h2>QC metrics preview</h2>
    {dataframe_to_html_table(qc_preview)}
  </div>
</body>
</html>
"""

    Path(args.output).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()