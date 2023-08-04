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