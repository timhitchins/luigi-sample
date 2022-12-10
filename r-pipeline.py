import luigi
from rpy2.robjects.packages import importr
import os

# Config params
# class GlobalParams(luigi.Config):
# NumberBooks = luigi.IntParameter(default=10)
# NumberTopWords = luigi.IntParameter(default=500)


class MakeRDS(luigi.Task):
    """
    Create a sample dataset and save to RDS.
    """

    Region = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(f"data/test-data-{self.Region}.rds")

    def run(self):
        base = importr("base")
        base.saveRDS(base.c(1, 2, 3), f"data/test-data-{self.Region}.rds")


class WrangleData(luigi.Task):
    """Read RDS and wrangle"""

    Region = luigi.Parameter()

    def requires(self):
        return MakeRDS(Region=self.Region)
