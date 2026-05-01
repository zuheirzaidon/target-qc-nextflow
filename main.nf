nextflow.enable.dsl = 2

include { CHUNK_REGIONS }      from './modules/chunk_regions'
include { GENERATE_CANDIDATES } from './modules/generate_candidates'
include { SCORE_CANDIDATES }    from './modules/score_candidates'
include { SELECT_TOP_DESIGNS }  from './modules/select_top_designs'
include { SIMULATE_QC_METRICS } from './modules/simulate_qc_metrics'
include { BUILD_GENE_SUMMARY }  from './modules/build_gene_summary'
include { MAKE_REPORT }         from './modules/make_report'


workflow {
    regions_ch = Channel.fromPath(params.input)

    chunks_ch = CHUNK_REGIONS(regions_ch)
    candidates_ch = GENERATE_CANDIDATES(chunks_ch)
    scored_ch = SCORE_CANDIDATES(candidates_ch)
    top_designs_ch = SELECT_TOP_DESIGNS(scored_ch)
    qc_ch = SIMULATE_QC_METRICS(top_designs_ch)
    gene_summary_ch = BUILD_GENE_SUMMARY(top_designs_ch, qc_ch)

    MAKE_REPORT(top_designs_ch, qc_ch, gene_summary_ch)
}