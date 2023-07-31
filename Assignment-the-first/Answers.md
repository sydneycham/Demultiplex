# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here: 

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | Biological Read | 101 | Phred+33 |
| 1294_S1_L008_R2_001.fastq.gz | Index | 8 | Phred+33 |
| 1294_S1_L008_R3_001.fastq.gz | Index | 8 | Phred+33 |
| 1294_S1_L008_R4_001.fastq.gz | Biological Read | 101 | Phred+33 |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.
    2. ![image](https://github.com/sydneycham/Demultiplexing/assets/115667425/702084fb-b66e-4879-83ee-a5e12e74581d)

    3. ![image](https://github.com/sydneycham/Demultiplexing/assets/115667425/488d8f24-ac40-484c-bef2-65b6c12123e2)
    4. ![image](https://github.com/sydneycham/Demultiplexing/assets/115667425/7211a962-c38f-4e0e-ab2c-e87598fb4266)
    5. ![image](https://github.com/sydneycham/Demultiplexing/assets/115667425/f74b5587-93f0-4c8e-8174-5a4343cdcda4)




    
## Part 2
1. Define the problem : We have outputs from a sequencer that we are demultiplex. We are also trying to find hopped, unknow, and matched indexes.
2. Describe output : The output will be 52 fastq files with modified headers that include indexes, 48 for matched indexes, 2 for unknown indexes; one for each read (1 and 4), and 2 for hopped indexes; one for each read (1 and 4). 
3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4. Pseudocode
   ```
   {
   Def rev_comp(index:string)-->complement:string
    ```This function will take an input DNA string with N's and produce a reverse complement string of that string```
    Make it into a dictionary,and call it comp_dictionary 
        The key is one nucleotide of genetic code
        The value is its corresponding base pair 
        Ex.... {A:T,T:A, G:C, C:G} 
    Then i will reverse the order of the sequence, and create a new string with the reverse compliment
    Return(complement)
Example:
Index: GTA
    Intermediate: ATG
Output:TAC
   
    3. We will have tests for each scenario we need (matched,index-hopped,unknown scenarios)
```
{
Open all four files and read them, in a while true loop execute these commands in order of least computationally intesnse to most computationally
    with open (4 read files, "r") as rf1,rf2,rf3,rf4:
        while true
            #get header (rf1,rf4)
            #get sequence (rf1,rf4)
            header=line
            sequence=line
            *do same on read file 3, but use our reverse complement function on the sequence line of these 
                *if N is present in sequence line or not in list of index: reverse complement, attach to header, and output to unknown
                *elif:
                    add the index-index to both fw and rv if fw_barcode=rv_barcode and output to matched 
                *elif: 
                    fw1=rev AND index in list: send to index hopped
}
 ```
6. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
