#!/usr/bin/env python
import bioinfo
import argparse
import gzip

def get_args():
    parser= argparse.ArgumentParser()
    parser.add_argument("-f1", "--filename1", help="Input filename1", required=True)
    parser.add_argument("-f2", "--filename2", help="Input filename2", required=True)
    parser.add_argument("-f3", "--filename3", help="Input filename3", required=True)
    parser.add_argument("-f4", "--filename4", help="Input filename4", required=True)
    #parser.add_argument("-o", "--output", help="Output filename", required=False)

    return parser.parse_args()
 
args = get_args()
f1=args.filename1
f2=args.filename2
f3=args.filename3
f4=args.filename4
#o=args.output

filename_dict={}
file="/projects/bgmp/shared/2017_sequencing/indexes.txt"
with open(file, "r") as fh:
    fh.readline()
    for line in fh:
        index=line.strip().split("\t")[4]
        for item in index:
            R1_matched=open("output/"+index+"_R1.fq","w")
            R2_matched=open("output/"+index+"_R2.fq","w")
            filename_dict[index]=(R1_matched,R2_matched)

unknown_file1=open("unknown_read1.fq","w")
unknown_file4=open("unknown_read2.fq","w")
matched_file1=open("matched_read1.fq","w")
matched_file4=open("matched_read2.fq","w")
hopped_file1=open("hopped_read1.fq","w")
hopped_file4=open("hopped_read2.fq","w")

#dictionary with known indexes as key, index code is the value
knowndict = {"GTAGCGTA":0,"AACAGCGA":0,"CTCTGGAT":0,"CACTTCAC":0,"CGATCGAT":0,"GATCAAGG":0,"TAGCCATG":0,"CGGTAATC":0,"TACCGGAT":0,"CTAGCTCA":0,"GCTACTCT":0,"ACGATCAG":0,"TATGGCAC":0,"TGTTCCGT":0,"GTCCTAAG":0,"TCGACAAG":0,"TCTTCGAC":0,"ATCATGCG":0,"ATCGTGGT":0,"TCGAGAGT":0,"TCGGATTC":0,"GATCTTGC":0,"AGAGTCCA":0,"AGGATAGC":0}

#initializing matched, hopped and unknown dictionaries
instances_dict = {"matched":0,"hopped":0,"unknown":0}

#empty dict to store mismatched pairs
unknown_dict = {}

indexpairs={}


def readfour(fh):
    """make function to read through four lines and returns all lines in record as tuple"""
    header=fh.readline().strip()
    seq=fh.readline().strip()
    plus=fh.readline().strip()
    qual=fh.readline().strip()
    return [header,seq,plus,qual]

def append_header(index1,index2,header):
    '''creates header for identical indexes where they are appended at end of header'''
    new_header=header +" "+ index1 + "-" + index2
    return new_header

#open all four files and write lines to new files
with gzip.open(f1, "rt") as fh1, gzip.open(f2, "rt") as fh2, gzip.open(f3, "rt") as fh3, gzip.open(f4, "rt") as fh4:
    while True:
        record_r1 = readfour(fh1)
        if record_r1 == ["","","",""]:
            break #breaking when reaches end of file where there are no more in tuples
        record_r2 = readfour(fh2)
        record_r3 = readfour(fh3)
        record_r4 = readfour(fh4)
        reverse_index = bioinfo.rev_comp(record_r3[1])
        #new_header = " " +record_r1[0]+" " +record_r2[1]+"-"+reverse_index

        #setting headers for each read1 and read4
        record_r1[0]=append_header(record_r2[1],reverse_index,record_r1[0])
        record_r4[0]=append_header(record_r2[1],reverse_index,record_r4[0])
        print(record_r1[0], record_r4[0])
        index=record_r2[1] 

        new_key=(index+'-'+reverse_index)

        if 'N' in index or 'N' in reverse_index:
            instances_dict["unknown"]+=1
            unknown_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            unknown_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
        elif index not in knowndict or reverse_index not in knowndict:
            instances_dict["unknown"]+=1
            unknown_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            unknown_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
        elif index in knowndict and index==reverse_index:
            knowndict[index]+=1
            instances_dict["matched"]+=1
            filename_dict[index][0].write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            filename_dict[index][1].write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
            if new_key in indexpairs:
                indexpairs[new_key]+=1
            else:
                indexpairs[new_key]=1
        elif index in knowndict and reverse_index in knowndict and index!=reverse_index:
            instances_dict["hopped"]+=1
            hopped_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            hopped_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
            if new_key in indexpairs:
                indexpairs[new_key]+=1
            else:
                indexpairs[new_key]=1

        #if record_r2[1] in knowndict and record_r2[1] == reverse_index:
            #instances_dict[matched]+=1
print (instances_dict)
print(indexpairs)

unknown_file1.close()
unknown_file4.close()
matched_file1.close()
matched_file4.close()
hopped_file1.close()
hopped_file4.close()