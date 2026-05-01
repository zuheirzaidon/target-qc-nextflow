process MAKE_REPORT {
    tag "${top_designs_csv.simpleName}"
    publishDir "${params.outdir}/report", mode: 'copy'

    input:
    path top_designs_csv
    path qc_csv

    output:
    path "report.txt"

    script:
    """
    make_report.py \
        --designs ${top_designs_csv} \
        --qc ${qc_csv} \
        --output report.txt
    """
}