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
