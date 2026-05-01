process MAKE_REPORT {
    tag "${top_designs_csv.simpleName}"
    publishDir "${params.outdir}/report", mode: 'copy'

    input:
    path top_designs_csv
    path qc_csv
    path gene_summary_csv

    output:
    path "report.html"

    script:
    """
    make_report.py \
        --designs ${top_designs_csv} \
        --qc ${qc_csv} \
        --gene-summary ${gene_summary_csv} \
        --output report.html
    """
}