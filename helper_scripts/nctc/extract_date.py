import pandas as pd
import re
import sys
# heuristic, first look in 'Isolated From', then look in 'History', then look in 'Data', then look in 'Other', then look in 'Accession Date', then look in 'Authority', then look in 'Bibliography', then say it's not here ya lil shit
x = pd.read_csv(sys.argv[1], sep='\t', index_col=0)
for index,row in x.iterrows():
    year_ext = None
    # super sexy regex to find year
    regex_for_year = "(?:19|20)\d{2}"
    i_f = re.findall(regex_for_year, str(row['Isolated_From']))
    if len(i_f)!=0:
        year_ext = min(i_f)
        if int(year_ext) > 2020: year_ext = None
    hist = re.findall(regex_for_year, str(row['History']))
    if len(hist)!=0 and year_ext==None:
        year_ext=min(hist)
        if int(year_ext) > 2020: year_ext = None
    data = re.findall(regex_for_year, str(row['Data']))
    if len(data)!=0 and year_ext==None:
        year_ext=min(data)
        if int(year_ext) > 2020: year_ext = None
    other = re.findall(regex_for_year, str(row['Other']))
    if len(other)!=0 and year_ext==None:
        year_ext=min(other)
        if int(year_ext) > 2020: year_ext = None
    auth = re.findall(regex_for_year, str(row['Authority']))
    if len(auth)!=0 and year_ext==None:
        year_ext=min(auth)
        if int(year_ext) > 2020: year_ext = None
    acc_date = re.findall(regex_for_year, str(row['Accession_Date']))
    if len(acc_date)!=0 and year_ext==None:
        year_ext=min(acc_date)
        if int(year_ext) > 2020: year_ext = None
    bib = re.findall(regex_for_year, str(row['Bibliography']))
    if len(bib)!=0 and year_ext==None:
        year_ext=min(bib)
        if int(year_ext) > 2020: year_ext = None
    if year_ext == None:
        print(row['NCTC_Number']+"\t"+"-1")
    else:
        print(row['NCTC_Number']+"\t"+year_ext)
