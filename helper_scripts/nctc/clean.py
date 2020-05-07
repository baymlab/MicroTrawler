import pandas as pd
import sys
# read in PHAT database
table = pd.read_csv(sys.argv[1], index_col=0, sep="\t")
# get the number of values in each column 
num_null = table.notnull().sum()
# pick out the ones with NOTHING
missing_features = num_null[num_null <  int(sys.argv[2])].index
# GETEMOUTOFHER
table.drop(missing_features, axis=1, inplace=True)
table.to_csv(sys.argv[1], sep="\t")
