process SELECT_TOP_DESIGNS {
    tag "${scored_csv.simpleName}"
    publishDir "${params.outdir}/selected", mode: 'copy'

    input:
    path scored_csv

    output:
    path "top_designs.csv"

    script:
    """
    select_top_designs.py \
        --input ${scored_csv} \
        --output top_designs.csv
    """
}