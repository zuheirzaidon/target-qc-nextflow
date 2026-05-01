process GENERATE_CANDIDATES {
    tag "${chunks_csv.simpleName}"
    publishDir "${params.outdir}/candidates", mode: 'copy'

    input:
    path chunks_csv

    output:
    path "candidates.csv"

    script:
    """
    generate_candidates.py \
        --input ${chunks_csv} \
        --output candidates.csv \
        --num-candidates ${params.candidates_per_chunk}
    """
}