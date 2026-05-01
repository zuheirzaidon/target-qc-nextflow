process CHUNK_REGIONS {
    tag "${regions_csv.simpleName}"
    publishDir "${params.outdir}/chunks", mode: 'copy'

    input:
    path regions_csv

    output:
    path "chunks.csv"

    script:
    """
    chunk_regions.py \
        --input ${regions_csv} \
        --output chunks.csv \
        --chunk-size ${params.chunk_size}
    """
}