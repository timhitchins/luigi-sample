save_rds <- function(region, name) {
    saveRDS(c(1, 2, 3), paste0("data/script-data-", name, region, ".rds"))
}

# Check if called from cli
if (sys.nframe() == 0) {
    args <- commandArgs(trailingOnly = TRUE)
    region <- args[1]
    name <- args[2]
    save_rds(region, name)
}
