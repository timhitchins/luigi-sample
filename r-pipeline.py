#!/home/timhitchins/Documents/virtualenvs/luigi/bin python3
import luigi
from rpy2.robjects.packages import importr
import rpy2.robjects as robjects
import subprocess

command = "/usr/lib/R/bin/Rscript"
arg = "--vanilla"
script = "/home/timhitchins/repos/luigi-sample/save_rds.R"
retcode = subprocess.call(
    [command, arg, script, "NW", "test"], stdout=subprocess.PIPE, shell=True
)
# retcode.communicate()

# # Config params
# # class GlobalParams(luigi.Config):
# # NumberBooks = luigi.IntParameter(default=10)
# # NumberTopWords = luigi.IntParameter(default=500)


# class SaveRDS(luigi.Task):
#     """
#     Create a sample dataset and save to RDS.
#     """

#     Region = luigi.Parameter(default=None)

#     def output(self):
#         return luigi.LocalTarget(f"data/rds-data-{self.Region}.rds")

#     def run(self):
#         base = importr("base")
#         base.saveRDS(base.c(1, 2, 3), f"data/rds-data-{self.Region}.rds")


# class CallRObj(luigi.Task):
#     """
#     Use R Object to call fun.
#     """

#     Region = luigi.Parameter(default=None)

#     def output(self):
#         return luigi.LocalTarget(f"data/script-data-{self.Region}.rds")

#     def run(self):
#         base = importr("base")
#         r = robjects.r
#         r.source("save_rds.R"),
#         r.save_rds(self.Region)


# class CallRScript(luigi.Task):
#     """
#     Run Rscript with .
#     """

#     Region = luigi.Parameter(default=None)

#     def output(self):
#         return luigi.LocalTarget(f"data/script-data-{self.Region}.rds")

#     def run(self):
#         command = "/usr/lib/R/bin/Rscript"
#         arg = "--vanilla"
#         script = "save_rds.R"
#         retcode = subprocess.call(
#             [command, arg, script, self.Region],
#             stdout=subprocess.PIPE,
#             shell=True)
#         retcode.communicate()


# class WrangleData(luigi.Task):
#     """Read RDS and wrangle"""

#     Region = luigi.Parameter(default=None)

#     def requires(self):
#         yield SaveRDS(Region=self.Region)
#         # yield CallRObj(Region=self.Region)
#         yield CallRScript(Region=self.Region)
