# MicroTrawler
🎣 - go fishing for bacterial accession numbers in public databases

## NCTC

To trawl the NCTC, clone and cd into the repo. Then,
```
chmod +x nctc_trawler
./nctc_trawler 
```

There are 4 options:
```
-o/--output : output file to dump NCTC db to. default is ./nctc_db.tsv
-s/--sleep : number of seconds to sleep before pinging NCTC again. default is 5
-m/--max : max NCTC accession number to search. default is curr. max. accession number in NCTC
-n/--min : min NCTC accession number to search. default is 1
```

The script basically loops through all NCTC numbers from the --min option to the --max option, and dumps all strain info found into --output.
