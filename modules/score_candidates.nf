process SCORE_CANDIDATES {
    tag "${candidates_csv.simpleName}"
    publishDir "${params.outdir}/scores", mode: 'copy'

    input:
    path candidates_csv

    output:
    path "scored_candidates.csv"

    script:
    """
    score_candidates.py \
        --input ${candidates_csv} \
        --output scored_candidates.csv
    """
}