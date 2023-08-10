Percentage of reads matched, hopped and unknown. 
{'matched': 331755033, 'hopped': 707740, 'unknown': 30783962}

Matched Index percentages can be found in [matched_indexes.md](matched_indexes.md)  

TACCGGAT-TACCGGAT has a very high proportion of reads, this could be due to overrepresentation of this sample in the pool. Unless this was intentional but without further clarification from the people wanting to run this I wouldn't know. In most cases though the reads should be fairly even across samples since most pools are made equimolar. 

Hopped index percentages can be found in [hopped_indexes.md](hopped_indexes.md)  

Nothing looks out of the ordinary to me here. 0.19% of indexes were hopped, a pretty small error rate.

Quality score cutoff: I chose a quality score of 2 inherently in my code structure of filtering out reads with 'N' in them. 
