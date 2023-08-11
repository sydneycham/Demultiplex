Lab_Notebook_Bi622
7-26-2023

Talapas path for fastq files
do not unzip files, use zcat
/projects/bgmp/shared/2017_sequencing
1294_S1_L008_R1_001.fastq.gz (Biological Read)
1294_S1_L008_R2_001.fastq.gz (Indexes)
1294_S1_L008_R3_001.fastq.gz  (Biological Read)
1294_S1_L008_R4_001.fastq.gz (Indexes)

Inital data exploration
zcat 1294_S1_L008_R1_001.fastq.gz | wc - l
gives us number of reads: 1.5 billion

to pull out headers
zcat 1294_S1_L008_R1_001.fastq.gz | grep "^@" | head


zcat 1294_S1_L008_R1_001.fastq.gz | grep -v "^@" | head -1 | wc

to find number of cycles
zcat 1294_S1_L008_R1_001.fastq.gz | grep -v "^@" | head -1 | wc -L
101
same for r4


7-27-2023

wrote test files (output and input) for the group so we can compare when we actually start running the code
R1_Test.fq
R2_Test.fq
R3_Test.fq
R4_Test.fq


to find number of cycles
zcat 1294_S1_L008_R2_001.fastq.gz | grep -v "^@" | head -1 | wc -L
8
same for read 3

7-28-2023


$ srun --account=bgmp --partition=compute --time=3:00:00 --pty bash 
./Histogram_script.py -f 1294_S1_L008_R1_001.fastq.gz -o r1_hist (for each file to generate histograms, they take forever)


7-31-2023

to get number of undetermined base calls
zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz | sed -n '2~4p' | grep "N" | wc -l 
3976613

zcat /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz | sed -n '2~4p' | grep "N" | wc -l 
3328051
Total read number: 363246735
r2 = (3976613/363246735)*100%= 1.09%
r3 = (3328051/363246735)*100%= 0.92%

8-7-2023

Defined a function in bioinfo called rev_comp to reverse complement a string of nucleotides

Path to desired files
    /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz 
    /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz 
    /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz  
    /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz   

Created a dictionary to hold the total amount of matched, hopped, and unknown instances and tally them
Created a dictionary to hold each matched index pairing and tally them, as well as another dictionary for hopped

Created a sum total for amount of records to use later in determining percentage of samples 
 
When opening the real files I have to unzip them so change to gzip.open and "rt"

Adding parts in if statements to account for the tallied index pairings
        


8-8-2023

Everything seems to be working on the test files so time to create a script to run this (demultiplex_slurm.sh)
    slurm-26264
    Submitted batch job 26264
Error wrong input files
Every other rerun was just to get more of what we wanted out of the results, adding little bits here and there
