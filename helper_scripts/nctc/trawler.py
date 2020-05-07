#!/bin/python3
import pandas as pd
import sys
import os.path

in_nctc = sys.argv[1]
out_db = sys.argv[2]

# read html table
x = pd.read_html(in_nctc,index_col=0)

# nothing here yet, leave
if len(x) == 0:
    sys.exit(2)

# get it all purty
full_info = x[0].T
better_col = {}
for ugly_col in full_info:
    sexy_col = ugly_col.replace(":","")
    sexy_col = sexy_col.replace(" ", "_")
    better_col[ugly_col] = sexy_col
full_info = full_info.rename(columns=better_col)

# look for extended bib table and slap it in
try:
    bib = "--".join(x[1].index.tolist())
    full_info["Extended_Bibliography"] = bib
except:
    pass

# append output if file already exists
if os.path.isfile(out_db):
    prev_db = pd.read_csv(out_db, sep='\t', index_col=0, dtype=str)
    full_info = prev_db.merge(full_info, how="outer")

# dump output to file
full_info.to_csv(out_db, sep='\t')
