# april 2020

## april 10
yeet. first day working on this. what's the plan mama jam? im gonna take ATCC, NCTC, and CIP. scrape'em for all bacterial accession numbers that meet certain criteria! 
I think I can just use shell scripts to meme on each page? let's first look at ATCC...

Ok based on curl ATCC output looks like a HOT mess. I could try interfacing with Python? But that's such a meme. Hopefully the other websites are not LITERAL
javascript trash

## april 13
Ok. I've spent some time looking through NCTC and CIP websites. They do seem more informative than ATCC, but tbh everything seems like it'll be a pain in the ass. 
I'll probably start looking for nice APIs to query websites in a GUI-centric fashion. Of note, I found a strain for which I would like to derive some info and analysis on.

It is Streptococcus gordonii. Allegedly cultured from a patient with gum disease (Pyorrhoea), it's accession numbers are: NCTC 3165, ATCC 33399, DSM 20568, CIP 103221. 
According to all collections, it was first deposited in 1930 by one D. Thomson of the Pickett-Thomson Research Laboratory to NCTC. But I cannot find any information
about the Pickett-Thomson Research Laboratory, all I can find with their name are reviews of a research magazine they used to publish called 'Annals of the Pickett-Thompson
Research Laboratory'.

## april 16

I think NCTC 3000 might be a cool resource to mine? Also, I should identify and look for programs that take fastq reads and predicts antibiotic resistance. I think this should probably? exist; however, I am unsure if this would necessitate a full genome assembly or I can take a kmer based approach. If the reads are not long, then I can imagine a kmer based approach would fail.

Also, NCTC 30; cholera from WWI shows antibiotic resistance gene. https://www.sanger.ac.uk/news/view/genetic-code-wwi-soldiers-cholera-mapped

DSMZ has predictable urls, but it's from a pdf

ATCC switched numbering scheme at some point
 
Ask what they can share first

NCTC 1 is first sample in culture collection --> shigella flexinari

CARD, antibiotic resistance database.

## april 22
Ok dab dab dab dab. NCTC trawler looks like it is working. Currently running it on everything. Gonna tackle ATCC and CIP next

# may 2020

## may 7

Got script to snag pre1940 ENA assemblies working. I think a couple next steps are warranted:
1. Get CIP trawler working 
2. Dl + analyze genomes looking for antibiotic resistance
3. Search SRA for sequences as well
4. Get ATCC trawler working 

## may 9

OK going to work on the CIP trawler. 

## may 15

CIP trawled. Got NCTC sequences. Made histogram of CIP dates, 37 strains have no discernable year information. 

Also, put a hard cap on NCTC date extractor, sent followup email to NCTC asking about how to accurately get year info.

## may 18
Got response from NCTC. I've been doing some dates wrong. turns out we don't know the info for a lot of bacterial species. 
Extracted the fasta assemblies for the ensembl files on o2. Every strain there now has a associated fasta file. going to now work on 
getting a script to look for antibiotic resistance using CARD.

## may 20
wrote ab finder using rgi. think I'm using it right? I think next step is to make a generalized framework to this project

Ok script is up and I ran it on NCTC assemblies. failed for like 4? (turns out I didn't get fastas for them.. need to figure out how) but got results for the remaining. I have to now understand what the output of `rgi` actually means and spot check a couple to make sure it's real.

I'm going to build a diagram for workflow now. going to try and make it using snakemake!

snakemake is hard. I don't like it.

## may 28

Moved everything to o2 and am in the process of writing scripts to run everything in a clean fashion. Wrote a function that should theoretically scrape ncbi refseq but it's a pain in the ass. Also trying to consolidate input and output formats for my scripts.

## june 2

Ok. I think I have successfully massaged the download_refseq and download_cip scripts to the correct format. I'm going to work on looking for ab resistance now.

## june 3

Submitted all the jobs looking for ab resistance. Currently I can't find any ancient strains from the CIP in the databases. Have to look into that but the format makes sense and I have a working example of everything.

## june 8

Lo, I have been played the fool. CIP sequences are also in ENA but they are 'CIP XXXX' instead of 'CIPXXXX'.

OK I fixed that so now I also search the ENA using 'CIP XXXX' and 'CIPXXXX'. In addition, added a tweak to the extract dates script. It now makes sure the year is a valid word.
