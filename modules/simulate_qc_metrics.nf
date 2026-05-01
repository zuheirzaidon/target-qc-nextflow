process SIMULATE_QC_METRICS {
    tag "${top_designs_csv.simpleName}"
    publishDir "${params.outdir}/qc", mode: 'copy'

    input:
    path top_designs_csv

    output:
    path "qc_metrics.csv"

    script:
    """
    simulate_qc_metrics.py \
        --input ${top_designs_csv} \
        --output qc_metrics.csv
    """
}