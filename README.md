# MicroTrawler
🎣 - go fishing for ancient antibiotic resistance in public databases

# GAMEPLAN

1. Download database [nctc_trawler, cip_trawler] to a tsv
2. Extract best guess for culture year for each strain [helper_scripts/nctc,cip/extract_dates]
3. Use awk to filter strains to pre-ab dates awk `{if($2<=1940){print $0}} $dates > ./ancient_strains`
4. Download existing uploaded assemblies found in ena/refseq for each `helper_scripts/generic/download_ena,download_refseq`
5. Search these fasta files for ABR using RGI `helper_scripts/generic/look_for_ab_resistance`

## NCTC

To trawl the NCTC, clone and cd into the repo. Then,
```
chmod +x nctc_trawler
./nctc_trawler 
```

There are 4 options:
```
-o/--output : output file to dump NCTC db to. default is ./YYYY-MM-DD_nctc_db.tsv
-s/--sleep : number of seconds to sleep before pinging NCTC again. default is 5
-m/--max : max NCTC accession number to search. default is curr. max. accession number in NCTC
-n/--min : min NCTC accession number to search. default is 1
-c/--clean : remove very sparse columns in final database. 'very sparse' is <= $clean number of total values in a given column. Default is 2 
```

The script basically loops through all NCTC numbers from the --min option to the --max option, and dumps all strain info found into --output. Requires `pandas` (install [here](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html))

## CIP

To trawl the CIP, clone and cd into the repo. Then,
```
chmod +x cip_trawler
./cip_trawler 
```

There are 2 options:
```
-o/--output : output file to dump CIP db to. default is ./YYYY-MM-DD_cip_db.tsv
-s/--search : search term to use. default is 'CIP' (this grabs all CIP entries in database)
```

The CIP is very nifty in that it already has a button to download everything as an excel spreadsheet!! :O This is still a programmatic option so you don't have to deal with websites. Theoretically we can access every search field. This requires `selenium` (see install instructions [here](https://selenium-python.readthedocs.io/installation.html)), `geckodriver` (install same as before), and `pandas` (install above)
