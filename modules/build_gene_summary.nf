process BUILD_GENE_SUMMARY {
    tag "${top_designs_csv.simpleName}"
    publishDir "${params.outdir}/gene_summary", mode: 'copy'

    input:
    path top_designs_csv
    path qc_csv

    output:
    path "gene_summary.csv"

    script:
    """
    build_gene_summary.py \
        --designs ${top_designs_csv} \
        --qc ${qc_csv} \
        --output gene_summary.csv
    """
}