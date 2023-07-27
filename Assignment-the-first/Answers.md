# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here:

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | Biological Read | 101 |  |
| 1294_S1_L008_R2_001.fastq.gz | Index | 8 |  |
| 1294_S1_L008_R3_001.fastq.gz | Index | 8 |  |
| 1294_S1_L008_R4_001.fastq.gz | Biological Read | 101 |  |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.
    2. **YOUR ANSWER HERE**
    3. **YOUR ANSWER HERE**
    
## Part 2
1. Define the problem : We have outputs from a sequencer that we are demultiplex. We are also trying to find hopped, unknow, and matched indexes.
2. Describe output : The output will be 52 fastq files with modified headers that include indexes, 48 for matched indexes, 2 for unknown indexes; one for each read (1 and 4), and 2 for hopped indexes; one for each read (1 and 4). 
3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
    /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz
    /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz
    /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz
    /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz
4. Pseudocode
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
